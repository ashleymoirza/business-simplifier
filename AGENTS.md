# AGENTS.md — Business Simplifier Multi-Agent Workstream Registry
*Last updated: 2026-05-25*

This file documents the five specialised workstreams (agents) for the Business Simplifier project, their scope, I/O contracts, dependencies, and ordering.

---

## Dependency Graph

```
Agent 1 (Content Engine) ──────────────────────────────┐
Agent 2 (GitHub Deploy) ─────── depends on Agent 1 ───┤
Agent 3 (GoDaddy DNS) ───────── depends on Agent 2 ───┼──→ LIVE SITE
Agent 4 (UI/UX Audit) ────────── depends on Agent 2 ───┤
Agent 5 (Backend Dashboard) ─── independent of 1-4 ───┘
```

Run Agent 1 → Agent 2 → Agents 3 & 4 in parallel → Agent 5 independently.

---

## Agent 1: Content Engine

**Scope:** Generate and publish all 30 SEO-optimised blog posts to the Astro website.

**Inputs:**
- `STRATEGY.md` Section 6 (30-day content calendar)
- `src/data/blogPosts.js` (existing 9 posts as style reference)
- `marketing.md` (brand voice, keyword targets, competitor context)

**Outputs:**
- Updated `src/data/blogPosts.js` with 30 total blog posts
- Each post: `{ slug, title, excerpt, content, category, author, publishedDate, readTime, tags }`
- Content requirements per post:
  - Minimum 400 words
  - At least 2 SA-specific statistics with source attribution
  - 1 CTA embedded (consultation booking)
  - Primary keyword in title, H2s, and first paragraph
  - No AI-slop: specific numbers, named businesses/regions, real ROI data

**Conventions:**
- Author: `'Business Simplifier Team'`
- Date format: `'YYYY-MM-DD'`
- Slugs: kebab-case, keyword-rich
- Tags: 3–5 per post, lowercase with spaces

**Error Handling:**
- If a stat cannot be verified, use hedging language ("research suggests", "industry estimates")
- Never fabricate specific company names as case study subjects without clear attribution

**Testing:**
- `npm run build` must complete with 0 errors
- All 30 slugs must be unique
- No undefined `category` values (must match `blogCategories` IDs)

---

## Agent 2: GitHub Deploy

**Scope:** Initialise git repository, create GitHub Actions CI/CD pipeline, push to GitHub, enable GitHub Pages.

**Inputs:**
- Built Astro project at `AI Consultation/`
- GitHub username (provided by user)
- `STRATEGY.md` Section 7 (deploy workflow YAML)

**Outputs:**
- `.github/workflows/deploy.yml` created
- `public/CNAME` file with custom domain
- `git init` + first commit + remote pushed
- GitHub Pages enabled with GitHub Actions source

**Shared Interfaces:**
- Output: Live URL format `https://USERNAME.github.io/REPO_NAME` (pre-custom domain)
- Output: `CNAME` file content (used by Agent 3)

**Conventions:**
- Branch: `main` (not `master`)
- Commit message: `"feat: initial website deploy — Business Simplifier AI"`
- `.gitignore` must exclude: `node_modules/`, `dist/`, `.DS_Store`, `.env`

**Error Handling:**
- If Actions build fails: check `astro.config.mjs` site URL matches domain
- If Pages not activating: ensure repo is public

**Dependencies:** Agent 1 must be complete (all posts in blogPosts.js) before first deploy

---

## Agent 3: GoDaddy DNS Configuration

**Scope:** Configure GoDaddy domain DNS records to point to GitHub Pages.

**Inputs:**
- GoDaddy account credentials (user provides)
- GitHub Pages IP addresses (from STRATEGY.md Section 7):
  - `185.199.108.153`
  - `185.199.109.153`
  - `185.199.110.153`
  - `185.199.111.153`
- Custom domain name (e.g., `businesssimplifier.co.za`)

**Outputs:**
- 4 x A records for root domain (@)
- 1 x CNAME record for `www` subdomain
- GitHub Pages HTTPS enforced
- SSL certificate issued automatically

**Verification:**
- DNS propagation check: `dig businesssimplifier.co.za A` → returns 4 GitHub IPs
- Online tool: dnschecker.org
- Expected propagation time: 15 min–48h

**Dependencies:** Agent 2 must have GitHub Pages live with custom domain set

---

## Agent 4: UI/UX Audit & Implementation

**Scope:** Measure the live site against industry standards and implement priority improvements.

**Inputs:**
- Live site URL (post Agent 2 & 3 completion)
- `STRATEGY.md` Section 8 (audit checklist)
- Astro/Tailwind source files in `src/`

**Outputs:**
- PageSpeed Insights score ≥ 90 (mobile + desktop)
- All CWV metrics in green
- New components implemented:
  - `src/components/TestimonialsSection.astro`
  - `src/components/TrustBar.astro` (social proof numbers)
  - `src/components/StickyMobileCTA.astro`
  - `src/components/ExitIntentPopup.astro` (Alpine.js)
- Accessibility fixes applied across all components
- Internal linking added to blog posts

**Priority Order (highest ROI first):**
1. Sticky mobile CTA → estimated +23% mobile conversions
2. Testimonials section → builds trust, reduces bounce
3. Exit-intent popup → captures 5-8% abandoning visitors
4. CWV fixes → Google ranking factor
5. Accessibility pass → WCAG 2.1 AA compliance

**Testing:**
- PageSpeed Insights: `https://pagespeed.web.dev`
- WCAG: axe DevTools browser extension
- Mobile: Chrome DevTools → iPhone 14 viewport

**Dependencies:** Agent 2 complete (requires live URL for testing)

---

## Agent 5: Backend Dashboard — AI Source Recommender

**Scope:** Design and build the AI-powered dashboard where sources are uploaded and AI implementation recommendations are generated.

**Inputs:**
- `STRATEGY.md` Section 9 (full architecture plan)
- Existing `server.py` and `api/` directory (reference patterns)
- Claude API access (Anthropic SDK)

**Outputs:**
- `dashboard/` directory with full project scaffold:
  - `dashboard/backend/` — FastAPI application
  - `dashboard/frontend/` — React + Vite application
- Working MVP features:
  - File upload (PDF, DOCX, XLSX, TXT, CSV)
  - Document parsing (PyMuPDF, python-docx, openpyxl)
  - Claude API integration with recommendation prompt
  - JSON response rendered as UI cards
  - Export to PDF
- Deployment config for Render.com (free tier)

**I/O Contract (API):**

```
POST /api/upload
  Input: multipart/form-data { file: File }
  Output: { document_id: str, filename: str, status: "uploaded" }

POST /api/analyse/{document_id}
  Input: { document_id: str }
  Output: { 
    document_id: str,
    summary: str,
    processes: [
      {
        name: str,
        description: str,
        aiSolution: str,
        toolType: str,
        timeSavedHours: int,
        costEstimateZAR: int,
        difficulty: int (1-5),
        priority: int (1-10)
      }
    ]
  }

GET /api/documents
  Output: [{ document_id, filename, uploaded_at, analysed: bool }]
```

**Shared Conventions (with existing codebase):**
- Python: follow patterns in `api/routes.py` and `api/services.py`
- Error handling: HTTP exceptions with descriptive messages
- Logging: Python `logging` module, INFO level
- No hardcoded API keys — use environment variables (`ANTHROPIC_API_KEY`)

**Dependencies:** 
- Independent of Agents 1–4
- Requires `ANTHROPIC_API_KEY` environment variable
- Node.js 22+ for frontend, Python 3.11+ for backend

---

## Shared Conventions (All Agents)

### Naming
- Files: kebab-case for Astro/JS, snake_case for Python
- Components: PascalCase
- Variables: camelCase (JS), snake_case (Python)

### Environment Variables
- Never commit `.env` files
- Always provide `.env.example` with key names and descriptions
- Document all required vars in README

### Testing Mandate
- Every agent must run a build/lint check before marking complete
- Agent 1: `npm run build` with 0 errors
- Agent 2: GitHub Actions green checkmark
- Agent 3: DNS propagation confirmed at dnschecker.org
- Agent 4: PageSpeed score ≥ 90
- Agent 5: `uvicorn main:app` starts without errors

### Error Escalation
- If blocked by missing credentials (GitHub, GoDaddy, Anthropic API key): document the blocker and provide exact instructions for the user to resolve it
- Never silently skip a step — note `⚠️ BLOCKED:` with clear resolution path
