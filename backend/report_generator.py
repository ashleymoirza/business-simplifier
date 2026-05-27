"""
report_generator.py — Assembles the full deep audit report.

Takes the crawl result, ranked automation opportunities, and form inputs,
then calls lib/llm.py to generate a rich, business-specific narrative.

All LLM calls go through lib/llm.py → free-claude-code server (already installed).
No external APIs. No paid services.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Allow importing lib/ from the repo root
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from lib.llm import complete_json, complete
from .crawler import CrawlResult
from .automation_map import AutomationOpportunity, get_ranked_opportunities


# ---------------------------------------------------------------------------
# Report data structure
# ---------------------------------------------------------------------------

from dataclasses import dataclass, field


@dataclass
class AuditReport:
    company: str
    domain: str
    industry_detected: str
    industry_selected: str
    industry_final: str
    tech_stack: list[dict]                   # [{"category": "CMS", "name": "WordPress"}]
    tech_gap_analysis: str                   # LLM-generated paragraph
    executive_summary: str                   # LLM-generated 2-3 sentence overview
    annual_saving_zar: str                   # e.g. "R145,000"
    payback_weeks_range: str                 # e.g. "4–7"
    opportunities: list[dict]                # Ranked, enriched opportunity dicts
    quick_wins: list[str]                    # 3 things to do this week for free
    roadmap_month1: str
    roadmap_month2: str
    roadmap_month3: str
    website_summary: str                     # What we found when we crawled the site
    website_status: str                      # "success" | "partial" | "blocked"
    all_possibilities: list[dict]            # Full ranked list — all automations considered
    whatsapp_cta_url: str                    # Pre-filled wa.me link


# ---------------------------------------------------------------------------
# Saving calculation
# ---------------------------------------------------------------------------

_INDUSTRY_BASE_SAVINGS = {
    "Healthcare & Wellness":         {"1–10": 68000,  "11–50": 145000, "51–200": 280000, "200+": 520000},
    "Financial Services":            {"1–10": 92000,  "11–50": 178000, "51–200": 340000, "200+": 680000},
    "E-commerce & Retail":           {"1–10": 75000,  "11–50": 155000, "51–200": 310000, "200+": 590000},
    "Education & EdTech":            {"1–10": 52000,  "11–50": 118000, "51–200": 235000, "200+": 420000},
    "Real Estate & Property":        {"1–10": 88000,  "11–50": 165000, "51–200": 295000, "200+": 510000},
    "Legal & Professional Services": {"1–10": 105000, "11–50": 210000, "51–200": 395000, "200+": 720000},
    "Manufacturing & Engineering":   {"1–10": 82000,  "11–50": 168000, "51–200": 325000, "200+": 610000},
    "Logistics & Supply Chain":      {"1–10": 78000,  "11–50": 152000, "51–200": 298000, "200+": 565000},
    "Hospitality & Tourism":         {"1–10": 58000,  "11–50": 122000, "51–200": 248000, "200+": 445000},
    "HR & Recruitment":              {"1–10": 70000,  "11–50": 148000, "51–200": 285000, "200+": 530000},
    "Media & Marketing":             {"1–10": 85000,  "11–50": 162000, "51–200": 308000, "200+": 575000},
    "Non-profit & NGO":              {"1–10": 42000,  "11–50": 88000,  "51–200": 165000, "200+": 310000},
    "Construction & Property Dev":   {"1–10": 72000,  "11–50": 145000, "51–200": 275000, "200+": 495000},
    "Agriculture & Agritech":        {"1–10": 55000,  "11–50": 110000, "51–200": 205000, "200+": 380000},
    "Professional Services":         {"1–10": 95000,  "11–50": 185000, "51–200": 355000, "200+": 660000},
}

_GOAL_MULTIPLIERS = {
    "cut-costs":    1.15,
    "save-time":    1.00,
    "grow-revenue": 1.20,
    "improve-cx":   0.90,
}

_DEFAULT_BASE_SAVINGS = {"1–10": 62000, "11–50": 128000, "51–200": 245000, "200+": 460000}


def _calculate_saving(industry: str, size: str, goal: str) -> str:
    base_map = _INDUSTRY_BASE_SAVINGS.get(industry, _DEFAULT_BASE_SAVINGS)
    base = base_map.get(size, base_map.get("1–10", 62000))
    multiplier = _GOAL_MULTIPLIERS.get(goal, 1.0)
    adjusted = round((base * multiplier) / 1000) * 1000
    return f"R{adjusted:,.0f}".replace(",", " ")


# ---------------------------------------------------------------------------
# LLM-powered narrative generation
# ---------------------------------------------------------------------------

def _generate_executive_summary(
    company: str,
    industry: str,
    size: str,
    pain: str,
    tech_stack: list[dict],
    top_opportunities: list[dict],
    annual_saving: str,
) -> str:
    """Generate a 2–3 sentence exec summary personalised to this business."""
    tech_names = [t["name"] for t in tech_stack[:5]] if tech_stack else []
    tech_str = ", ".join(tech_names) if tech_names else "standard tools"
    top_titles = [o["title"] for o in top_opportunities[:3]]

    prompt = (
        f"You are writing an executive summary for an AI audit report for a South African SME.\n\n"
        f"Business: {company}\n"
        f"Industry: {industry}\n"
        f"Size: {size} employees\n"
        f"Current tools detected: {tech_str}\n"
        f"Main pain points: {pain}\n"
        f"Top automation opportunities identified: {', '.join(top_titles)}\n"
        f"Estimated annual saving: {annual_saving}\n\n"
        f"Write 2–3 sentences that:\n"
        f"1. Name the company and acknowledge their specific situation\n"
        f"2. State the single biggest automation opportunity clearly\n"
        f"3. Give the annual saving figure with confidence\n\n"
        f"Be direct, specific, and concrete. No generic AI hype. Use South African context. "
        f"Write in second person ('your business', 'your team'). Max 80 words."
    )
    try:
        return complete(prompt, temperature=0.4)
    except Exception:
        return (
            f"{company} has clear, high-value automation opportunities in {industry}. "
            f"Based on your team size, current tools, and stated pain points, the highest-ROI "
            f"starting point is {top_titles[0] if top_titles else 'process automation'}. "
            f"Implementing the recommendations below is estimated to save {annual_saving} per year."
        )


def _generate_tech_gap_analysis(
    company: str,
    tech_stack: list[dict],
    industry: str,
    pain: str,
) -> str:
    """Generate a paragraph analysing what the tech stack reveals about automation gaps."""
    if not tech_stack:
        return (
            f"No major platforms were detected on {company}'s website. This typically indicates "
            f"the business is running on basic tools — spreadsheets, email, and WhatsApp — "
            f"which means automation opportunities are abundant and the implementation baseline is clean."
        )

    tech_by_category: dict[str, list[str]] = {}
    for t in tech_stack:
        tech_by_category.setdefault(t["category"], []).append(t["name"])

    has_cms = "CMS" in tech_by_category
    has_crm = "CRM" in tech_by_category
    has_accounting = "Accounting" in tech_by_category
    has_booking = "Booking" in tech_by_category
    has_analytics = "Analytics" in tech_by_category
    has_email = "Email" in tech_by_category
    has_chat = "Chat" in tech_by_category

    gaps = []
    if not has_crm:
        gaps.append("no CRM or lead management layer")
    if not has_booking:
        gaps.append("no automated booking or scheduling system")
    if not has_email:
        gaps.append("no email marketing or nurture automation")
    if not has_analytics or all("Google" not in n for n in tech_by_category.get("Analytics", [])):
        gaps.append("limited performance tracking and reporting")
    if not has_chat:
        gaps.append("no automated customer communication or chatbot layer")

    tech_str = "; ".join(
        f"{cat}: {', '.join(names)}" for cat, names in tech_by_category.items()
    )

    prompt = (
        f"Analyse this tech stack for a South African {industry} business ({company}) "
        f"and identify the automation gaps.\n\n"
        f"Detected stack: {tech_str}\n"
        f"Pain points stated: {pain}\n"
        f"Identified gaps: {', '.join(gaps) if gaps else 'stack appears reasonably complete'}\n\n"
        f"Write 2–3 sentences that:\n"
        f"1. Acknowledge what they already have (don't dismiss existing tools)\n"
        f"2. Name the 2 biggest missing automation layers\n"
        f"3. Explain specifically how those gaps connect to the pain points they mentioned\n\n"
        f"Be technical and specific. Max 80 words. No generic statements."
    )
    try:
        return complete(prompt, temperature=0.3)
    except Exception:
        detected = ", ".join(t["name"] for t in tech_stack[:4])
        gap_str = ", ".join(gaps[:2]) if gaps else "workflow automation"
        return (
            f"{company} already runs {detected}. The main automation gaps identified are "
            f"{gap_str} — both of which directly contribute to the manual workload described above. "
            f"The recommendations below are designed to integrate with your existing stack."
        )


def _generate_quick_wins(
    company: str,
    industry: str,
    tech_stack: list[dict],
    pain: str,
    top_opp_titles: list[str],
) -> list[str]:
    """Generate 3 actionable free quick wins for this specific business."""
    tech_names = [t["name"] for t in tech_stack[:5]]
    prompt = (
        f"Generate exactly 3 quick wins for {company}, a {industry} business in South Africa.\n\n"
        f"Current tools: {', '.join(tech_names) if tech_names else 'basic tools'}\n"
        f"Pain points: {pain}\n"
        f"Top recommended automations: {', '.join(top_opp_titles[:3])}\n\n"
        f"Each quick win must:\n"
        f"- Be completable this week\n"
        f"- Cost R0 (use free tiers, existing tools, or built-in features)\n"
        f"- Be specific (name the exact tool or feature to use)\n"
        f"- Take under 2 hours to set up\n\n"
        f"Return JSON: {{\"wins\": [\"win 1\", \"win 2\", \"win 3\"]}}"
    )
    try:
        result = complete_json(prompt, schema={"required": ["wins"]})
        return result.get("wins", [])[:3]
    except Exception:
        return [
            "Set up WhatsApp Business with auto-replies for your 5 most common questions — free, takes 30 min",
            "Use Claude.ai or ChatGPT free tier to draft your next 10 customer emails in 20 minutes",
            "Connect your intake form to a Google Sheet with Zapier free plan — eliminates manual data entry",
        ]


def _generate_roadmap(
    company: str,
    industry: str,
    top_opportunities: list[dict],
) -> tuple[str, str, str]:
    """Generate a 3-month implementation roadmap."""
    opp_list = "\n".join(
        f"- {o['title']} (effort: {o['difficulty']}, payback: {o['paybackWeeks']} weeks)"
        for o in top_opportunities[:6]
    )
    prompt = (
        f"Create a practical 90-day AI implementation roadmap for {company} ({industry}) "
        f"based on these ranked automation opportunities:\n{opp_list}\n\n"
        f"Rules:\n"
        f"- Month 1: quick wins and foundations (Low difficulty items first)\n"
        f"- Month 2: core automation layer (highest ROI items)\n"
        f"- Month 3: advanced integrations and optimisation\n\n"
        f"Each month description: 1 sentence, specific, actionable. Name the actual automations.\n\n"
        f"Return JSON: {{\"month1\": \"...\", \"month2\": \"...\", \"month3\": \"...\"}}"
    )
    try:
        result = complete_json(prompt, schema={"required": ["month1", "month2", "month3"]})
        return result["month1"], result["month2"], result["month3"]
    except Exception:
        sorted_opps = sorted(top_opportunities, key=lambda o: (
            0 if o.get("difficulty") == "Low" else 1 if o.get("difficulty") == "Medium" else 2
        ))
        m1 = f"Deploy {sorted_opps[0]['title']} to establish the automation foundation and capture quick wins."
        m2 = f"Roll out {sorted_opps[1]['title'] if len(sorted_opps) > 1 else 'core process automation'} for the highest ROI gains."
        m3 = "Integrate all systems, refine workflows, and measure ROI against baseline metrics."
        return m1, m2, m3


# ---------------------------------------------------------------------------
# Main report builder
# ---------------------------------------------------------------------------

def build_report(
    form: dict,
    crawl_result: CrawlResult | None,
) -> AuditReport:
    """
    Build a complete deep audit report from form inputs and crawl data.

    Args:
        form: Dict with keys: company, industry, size, revenue, pain, tools, goal, website
        crawl_result: CrawlResult from crawler.crawl() — can be None if crawl failed

    Returns:
        AuditReport dataclass
    """
    company = form.get("company", "Your Business")
    selected_industry = form.get("industry", "")
    size = form.get("size", "1–10")
    pain = form.get("pain", "")
    tools_text = form.get("tools", "")
    goal = form.get("goal", "save-time")
    website = form.get("website", "")

    # ── Tech stack ───────────────────────────────────────────────────────────
    tech_stack: list[dict] = []
    inferred_industry = ""
    domain = ""
    website_status = "not_provided"
    website_summary = ""

    if crawl_result:
        domain = crawl_result.domain
        if crawl_result.error:
            website_status = "blocked"
            website_summary = (
                f"We attempted to scan {domain} but encountered: {crawl_result.error}. "
                f"Recommendations are based entirely on your manual inputs."
            )
        else:
            website_status = "success"
            tech_stack = crawl_result.detected_tech
            inferred_industry = crawl_result.inferred_industry
            tech_names = [t["name"] for t in tech_stack] if tech_stack else []
            if tech_names:
                website_summary = (
                    f"Successfully crawled {domain}. "
                    f"Detected: {', '.join(tech_names[:6])}. "
                    f"Recommendations have been tailored to integrate with your existing stack."
                )
            else:
                website_summary = (
                    f"Crawled {domain} — no major third-party platforms detected. "
                    f"This suggests a lean tech stack with significant automation headroom."
                )
    elif website:
        website_status = "partial"
        website_summary = "Website URL provided but could not be crawled. Recommendations based on manual inputs."

    # ── Resolve industry ─────────────────────────────────────────────────────
    industry_final = selected_industry or inferred_industry or "General Business"

    # ── Rank opportunities ───────────────────────────────────────────────────
    tech_names = [t["name"] for t in tech_stack]
    combined_pain = f"{pain} {tools_text}"

    ranked = get_ranked_opportunities(
        detected_tech_names=tech_names,
        inferred_industry=inferred_industry,
        pain_text=combined_pain,
        selected_industry=selected_industry,
        top_n=8,
    )

    # All possibilities (for internal view) — import here to avoid circular
    from .automation_map import AUTOMATIONS, score_opportunity
    all_scored = sorted(
        [(opp, score_opportunity(opp, tech_names, inferred_industry, combined_pain, selected_industry))
         for opp in AUTOMATIONS],
        key=lambda x: x[1], reverse=True,
    )

    def opp_to_dict(opp: AutomationOpportunity, score: int) -> dict:
        return {
            "id": opp.id,
            "title": opp.title,
            "category": opp.category,
            "description": opp.description,
            "buildApproach": opp.build_approach,
            "customBuildDetail": opp.custom_build_detail,
            "freeToolAlternative": opp.free_tool_alternative,
            "timeSavedHrs": opp.monthly_time_saved_hrs,
            "setupCostZar": opp.setup_cost_zar,
            "monthlyCostZar": opp.monthly_cost_zar,
            "paybackWeeks": opp.payback_weeks,
            "difficulty": opp.difficulty,
            "demoId": opp.demo_id,
            "demoLabel": opp.demo_label,
            "relevanceScore": score,
        }

    top_opps_dicts = [opp_to_dict(opp, score) for opp, score in ranked]
    all_opps_dicts = [opp_to_dict(opp, score) for opp, score in all_scored]

    # ── Financial calculations ───────────────────────────────────────────────
    annual_saving = _calculate_saving(industry_final, size, goal)
    payback_min = min((o["paybackWeeks"] for o in top_opps_dicts[:3]), default=4)
    payback_max = max((o["paybackWeeks"] for o in top_opps_dicts[:3]), default=8)
    payback_range = f"{payback_min}–{payback_max}"

    # ── LLM narrative generation ─────────────────────────────────────────────
    exec_summary = _generate_executive_summary(
        company, industry_final, size, pain, tech_stack, top_opps_dicts, annual_saving
    )
    tech_gap = _generate_tech_gap_analysis(company, tech_stack, industry_final, pain)
    quick_wins = _generate_quick_wins(
        company, industry_final, tech_stack, pain,
        [o["title"] for o in top_opps_dicts[:3]]
    )
    m1, m2, m3 = _generate_roadmap(company, industry_final, top_opps_dicts)

    # ── WhatsApp CTA ─────────────────────────────────────────────────────────
    import urllib.parse
    wa_message = (
        f"Hi, I've just completed an AI audit for {company} on businesssimplifier.co.za "
        f"and I'd like to discuss implementing the recommendations — particularly "
        f"{top_opps_dicts[0]['title'] if top_opps_dicts else 'the automation plan'}."
    )
    wa_url = f"https://wa.me/27000000000?text={urllib.parse.quote(wa_message)}"

    return AuditReport(
        company=company,
        domain=domain,
        industry_detected=inferred_industry,
        industry_selected=selected_industry,
        industry_final=industry_final,
        tech_stack=tech_stack,
        tech_gap_analysis=tech_gap,
        executive_summary=exec_summary,
        annual_saving_zar=annual_saving,
        payback_weeks_range=payback_range,
        opportunities=top_opps_dicts,
        quick_wins=quick_wins,
        roadmap_month1=m1,
        roadmap_month2=m2,
        roadmap_month3=m3,
        website_summary=website_summary,
        website_status=website_status,
        all_possibilities=all_opps_dicts,
        whatsapp_cta_url=wa_url,
    )
