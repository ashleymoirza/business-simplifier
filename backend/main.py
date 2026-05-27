"""
main.py — FastAPI backend for the BusinessSimplifier deep audit tool.

Endpoints:
  POST /api/audit       — full deep audit (crawl + AI analysis + report)
  POST /api/audit/quick — fast rule-based audit (no crawl, no LLM) for instant results
  GET  /api/health      — health check

Run with:
  cd "AI Consultation"
  uv run uvicorn backend.main:app --port 8001 --reload

The Astro site calls this from the browser via fetch('/api/audit').
In production: run this alongside the static site on the same VPS,
proxied via nginx so /api/* routes to this FastAPI server.
"""

from __future__ import annotations

import asyncio
import dataclasses
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator

from .crawler import crawl
from .report_generator import build_report


# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: warm up the LLM connection
    yield
    # Shutdown: nothing to clean up


app = FastAPI(
    title="BusinessSimplifier Audit API",
    description="Deep AI audit engine for South African SMEs",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://businesssimplifier.co.za",
        "https://www.businesssimplifier.co.za",
        "http://localhost:4321",   # Astro dev server
        "http://localhost:3000",
    ],
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type", "Authorization"],
)


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------

class AuditRequest(BaseModel):
    company: str
    industry: str = ""
    size: str = "1–10"
    revenue: str = ""
    pain: str
    tools: str = ""
    goal: str = "save-time"
    website: str = ""
    deep: bool = True   # If False, skip crawl and LLM — return rule-based instant report

    @field_validator("company")
    @classmethod
    def company_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Company name is required")
        return v

    @field_validator("pain")
    @classmethod
    def pain_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Pain points description is required")
        return v

    @field_validator("website")
    @classmethod
    def normalise_url(cls, v: str) -> str:
        v = v.strip()
        if v and not v.startswith(("http://", "https://")):
            v = "https://" + v
        return v


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "businesssimplifier-audit-api"}


@app.post("/api/audit")
async def deep_audit(req: AuditRequest):
    """
    Full deep audit:
    1. Crawl the website (if provided)
    2. Detect tech stack
    3. Rank automation opportunities
    4. Generate AI narrative via lib/llm.py
    5. Return complete report JSON

    Typically takes 5–15 seconds depending on site speed and LLM response time.
    """
    form = req.model_dump()

    # ── Step 1: Crawl website ─────────────────────────────────────────────
    crawl_result = None
    if req.website and req.deep:
        try:
            # Run in thread pool so we don't block the event loop
            loop = asyncio.get_event_loop()
            crawl_result = await loop.run_in_executor(None, crawl, req.website)
        except Exception as e:
            # Crawl failure is non-fatal — continue without it
            crawl_result = None

    # ── Step 2: Build report ──────────────────────────────────────────────
    try:
        loop = asyncio.get_event_loop()
        report = await loop.run_in_executor(None, build_report, form, crawl_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Report generation failed: {e}")

    # ── Step 3: Serialise dataclass to dict ───────────────────────────────
    return dataclasses.asdict(report)


@app.post("/api/audit/quick")
async def quick_audit(req: AuditRequest):
    """
    Fast rule-based audit — no crawl, no LLM calls.
    Returns in under 200ms. Used for instant preview while deep audit loads.
    """
    form = req.model_dump()
    try:
        loop = asyncio.get_event_loop()
        # Pass no crawl result — pure rule-based scoring
        report = await loop.run_in_executor(None, build_report, form, None)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Quick audit failed: {e}")

    return dataclasses.asdict(report)
