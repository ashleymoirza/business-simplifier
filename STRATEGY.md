# Optimal AI / Business Simplifier — Strategic Roadmap v2.0
*Last updated: 2026-05-25 | Scope: 30-Day Content Engine + GitHub Launch + Dashboard Plan*

---

## 1. Primary Objective & Measurable Success Criteria

**Objective:** Establish Business Simplifier as the dominant "AI for SMEs" brand in South Africa, ranking for every major AI consulting keyword vertical, generating inbound leads from organic search, and operating a live website on a custom GoDaddy domain — all within 30 days.

### Success Criteria

| Metric | Baseline | 30-Day Target | 90-Day Target |
|---|---|---|---|
| Organic clicks (GSC) | 0 | 500+ | 10,000+ |
| Indexed blog posts | 9 | 30 | 100+ |
| Keyword top-10 rankings | 0 | 15 | 80+ |
| Leads generated | 0 | 15 | 75+ |
| Paying clients | 0 | 5 | 25+ |
| Page speed (LCP) | Unknown | <2.5s | <2.0s |
| Core Web Vitals pass rate | Unknown | 100% | 100% |
| Bounce rate | – | <45% | <35% |
| GitHub repo live | ❌ | ✅ | ✅ |
| Custom domain live | ❌ | ✅ | ✅ |

---

## 2. Strategic Dimensions (Priority Order)

### [P1] Content Engine — 30-Day Calendar (CRITICAL PATH)
- **Goal:** 30 SEO-optimised blog posts live by Day 30 covering all 9 verticals
- **New angle:** "Free Website Makeover" + "AI Enhancements" posts as lead magnets
- **Keyword strategy:** Target informational → commercial → transactional intent funnel
- **Publishing schedule:** 1 post per day for 30 days (see Section 6)
- **Author persona:** Business Simplifier Team (builds brand trust vs. individual)

### [P2] GitHub Deployment Pipeline
- **Target host:** GitHub Pages (free, zero-downtime, CDN-backed)
- **Workflow:** `main` branch → Astro build → deploy to `gh-pages` via GitHub Actions
- **Custom domain:** Point GoDaddy domain to GitHub Pages (see Section 7)
- **SSL:** Automatic via GitHub Pages (Let's Encrypt)

### [P3] UI/UX Excellence
- **Framework:** WCAG 2.1 AA compliance + Google CWV standards
- **Conversion design:** Heat map principles applied to CTA placement
- **Mobile-first:** 70%+ SA web traffic is mobile (see Section 8 for audit results)

### [P4] Backend Dashboard — AI Source Recommender
- **Vision:** Upload any business document/source → AI analyses → recommends specific AI tools
- **Architecture:** FastAPI backend + React dashboard + Claude API
- **Phases:** MVP (6 weeks) → Beta (10 weeks) → Launch (12 weeks)
- **See Section 9 for full technical plan**

### [P5] GoDaddy Domain Configuration
- **Step-by-step:** Section 7

---

## 3. Key Risks, Assumptions & Contingencies

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Google sandbox (new domain) | High | Medium | Submit sitemap to GSC immediately; build internal links |
| Low organic traffic first 6 weeks | High | Medium | LinkedIn outreach as primary channel while SEO matures |
| GoDaddy DNS propagation delay | Low | Low | Allow 24–48h; use DNS checker tools |
| GitHub Actions build failure | Low | Medium | Test build locally first; use `astro build` pre-push |
| Content quality dilution | Medium | High | Use data + SA-specific stats in every post |

---

## 4. Assumptions

1. You have a GoDaddy account with a domain purchased (or will purchase one)
2. You have a GitHub account (free tier is sufficient)
3. Node.js ≥ 22.12.0 is installed locally
4. The Astro project at `AI Consultation/` is the source of truth for the website

---

## 5. Phase Execution Tracker

### Phase 1: Foundation ✅ COMPLETE (Days 1–3)
- [x] STRATEGY.md v1 created
- [x] Astro + Tailwind project initialized
- [x] Brand identity: Business Simplifier / optimalai.com
- [x] Core pages: Home, Services, About, Contact, Blog, Pricing
- [x] SEO foundation: sitemap, robots.txt, meta framework, JSON-LD schema
- [x] 9 initial blog posts across 8 verticals

### Phase 2: Content Engine ✅ COMPLETE (Days 4–7)
- [x] Blog system with categories
- [x] FAQ-trained AI chatbot
- [x] Pricing tables (SA ZAR + International USD)
- [x] SOP.md + MARKETING.md documented

### Phase 3: 30-Day Content Scale 🚀 IN PROGRESS (Days 8–30)
- [x] STRATEGY.md v2 updated with content calendar
- [ ] 21 new blog posts added (brings total to 30)
- [ ] Free Website Makeover offer page/post
- [ ] AI Enhancement explainer series
- [ ] GitHub repo created + CI/CD pipeline live
- [ ] GoDaddy domain pointed to GitHub Pages
- [ ] Google Search Console verified

### Phase 4: UI/UX Upgrade 🔧 (Days 8–14)
- [ ] Core Web Vitals audit (PageSpeed Insights)
- [ ] Mobile UX review — hero, CTA, nav
- [ ] Accessibility pass (colour contrast, aria labels, focus states)
- [ ] Trust signal improvements (testimonials section, social proof bar)
- [ ] Exit-intent / sticky CTA implementation

### Phase 5: Backend Dashboard MVP (Weeks 6–12)
- [ ] Tech stack confirmed
- [ ] FastAPI scaffold
- [ ] File upload + document parsing
- [ ] Claude API integration for AI tool recommendations
- [ ] React dashboard UI
- [ ] Beta testing with first 3 clients

---

## 6. 30-Day Content Calendar

> All posts target Business Simplifier brand. Primary domain: `businesssimplifier.co.za`.
> Existing 9 posts = Days 1–9. New 21 posts = Days 10–30.

| Day | Title | Primary Keyword | Intent | Vertical |
|-----|-------|----------------|--------|----------|
| 1 | AI in Healthcare: Transforming Patient Care in SA | ai healthcare south africa | Info | Healthcare |
| 2 | AI for Financial Services: Automation, Compliance, and Growth | ai financial services | Info | Finance |
| 3 | AI in E-commerce: Personalisation That Drives Revenue | ai ecommerce personalisation | Info | E-commerce |
| 4 | AI in Education: Personalised Learning at Scale | ai education south africa | Info | Education |
| 5 | AI for Small Business: A Practical Guide | ai for small business | Info | General |
| 6 | AI in Real Estate: Smarter Lead Generation | ai real estate south africa | Info | Real Estate |
| 7 | AI for Legal: Document Review and Contract Analysis | ai legal document review | Info | Legal |
| 8 | AI in Manufacturing: Quality Control and Automation | ai manufacturing quality control | Info | Manufacturing |
| 9 | AI in Logistics: Route Optimisation and Fleet Management | ai logistics route optimisation | Info | Logistics |
| 10 | Free Website Makeover: How AI Transforms Your Online Presence | free website makeover ai | Commercial | General |
| 11 | AI Chatbot for Business: Complete Setup Guide 2026 | ai chatbot for business | Commercial | General |
| 12 | How to Automate Your Customer Service With AI (Without Losing the Human Touch) | automate customer service ai | Info/Comm | General |
| 13 | AI Enhancements for SMEs: 10 Quick Wins You Can Implement This Week | ai enhancements small business | Commercial | General |
| 14 | Free AI Consultation: What to Expect and Why It's Worth Your Time | free ai consultation | Transactional | General |
| 15 | AI for Restaurants and Hospitality: Cut Costs, Fill Tables | ai restaurant hospitality | Info | Hospitality |
| 16 | AI for HR and Recruitment: Hire Smarter, Not Harder | ai hr recruitment south africa | Info | HR |
| 17 | AI for Accounting Firms: Automate the Boring, Focus on Strategy | ai accounting automation | Info | Finance |
| 18 | How Much Does AI Cost? Honest Pricing for SA Businesses | how much does ai cost south africa | Info | General |
| 19 | AI vs No AI: The Real Cost of Doing Nothing in 2026 | cost of not using ai | Info | General |
| 20 | 5 Signs Your Business Needs AI Automation (Right Now) | signs business needs ai | Info | General |
| 21 | Best AI Tools for South African Businesses in 2026 | best ai tools south africa 2026 | Info | General |
| 22 | WhatsApp AI Chatbot for Business: The SA Playbook | whatsapp ai chatbot business | Commercial | General |
| 23 | AI Website Audit: Is Your Website Leaving Money on the Table? | ai website audit | Commercial | General |
| 24 | AI for Property Management: Automate Maintenance and Tenant Queries | ai property management | Info | Real Estate |
| 25 | AI in Retail: Smart Inventory, Smarter Promotions | ai retail inventory south africa | Info | Retail |
| 26 | How We Build AI Chatbots (Step-by-Step Behind the Scenes) | how to build ai chatbot | Info | General |
| 27 | AI for Professional Services: Law, Accounting, Consulting | ai professional services | Info | General |
| 28 | The ROI of AI: Real Numbers From Real SA Businesses | roi of ai south africa | Info/Comm | General |
| 29 | AI Content Marketing: Get More Leads With Less Effort | ai content marketing south africa | Commercial | Marketing |
| 30 | Your 90-Day AI Roadmap: From Zero to Automated | 90 day ai roadmap small business | Transactional | General |

---

## 7. GitHub + GoDaddy Domain Setup (Step-by-Step)

### Step 1: Push Website to GitHub

```bash
# Navigate to the project folder
cd "AI Consultation"

# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: Business Simplifier AI website"

# Create repo on GitHub (via GitHub CLI or manually)
# Go to github.com → New Repository → name: "business-simplifier" → Public → Create

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/business-simplifier.git
git branch -M main
git push -u origin main
```

### Step 2: Set Up GitHub Actions for Auto-Deploy

Create `.github/workflows/deploy.yml` in the project root:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - name: Install dependencies
        run: npm ci
      - name: Build with Astro
        run: npm run build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Step 3: Enable GitHub Pages
1. Go to your GitHub repo → **Settings** → **Pages**
2. Under **Source**, select **GitHub Actions**
3. Your site will be live at `https://YOUR_USERNAME.github.io/business-simplifier`

### Step 4: Add Custom Domain in GitHub Pages
1. Go to repo → **Settings** → **Pages** → **Custom domain**
2. Type your domain (e.g., `www.businesssimplifier.co.za`) → Save
3. GitHub will create a `CNAME` file in your repo automatically

### Step 5: Configure GoDaddy DNS

**Login to GoDaddy → My Products → DNS Management for your domain**

#### If pointing ROOT domain (businesssimplifier.co.za):
Add 4 x **A Records** pointing to GitHub's IPs:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 600 |
| A | @ | 185.199.109.153 | 600 |
| A | @ | 185.199.110.153 | 600 |
| A | @ | 185.199.111.153 | 600 |

#### If pointing WWW subdomain:
| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | YOUR_USERNAME.github.io | 600 |

#### Both (recommended — do both for full coverage):
Add all 4 A records above + the CNAME for www.

### Step 6: Enable HTTPS in GitHub
- After DNS propagates (15–60 min usually, up to 48h): GitHub Pages Settings → **Enforce HTTPS** ✅
- Your site now serves on `https://businesssimplifier.co.za` with free SSL

### Step 7: Update astro.config.mjs
```js
export default defineConfig({
  site: 'https://businesssimplifier.co.za', // ← already set correctly
  integrations: [alpinejs()],
});
```

### Verification Checklist
- [ ] DNS propagated: check at [dnschecker.org](https://dnschecker.org)
- [ ] Site loads at custom domain
- [ ] HTTPS green lock shows
- [ ] `/blog` and `/services` pages load correctly
- [ ] No mixed content warnings in browser console

---

## 8. UI/UX Audit — Industry Best Practice Analysis

### Current Site Strengths ✅
- Clean navy/cyan brand palette (high contrast, professional)
- Data-driven hero copy (R135K saving stat = specific, credible)
- Mobile-responsive Tailwind grid
- Chatbot widget for engagement
- JSON-LD structured data implemented

### Improvement Areas (Industry Standard Benchmarks)

#### A. Core Web Vitals (Google 2026 Ranking Factor)
| Metric | Target | Action Required |
|--------|--------|----------------|
| LCP (Largest Contentful Paint) | <2.5s | Preload hero fonts; compress any images |
| CLS (Cumulative Layout Shift) | <0.1 | Add explicit width/height to all imgs |
| INP (Interaction to Next Paint) | <200ms | Defer non-critical JS (chatbot init) |
| FCP (First Contentful Paint) | <1.8s | Inline critical CSS |

#### B. Conversion Design (CRO Best Practices)
| Area | Current | Best Practice | Fix |
|------|---------|--------------|-----|
| CTA above fold | ✅ Present | ✅ | Keep |
| Social proof (client logos/testimonials) | ❌ Missing | Required | Add testimonials section |
| Trust badges | ❌ Missing | Increases conversion 15-20% | Add "100+ SA businesses served" badge |
| Exit intent popup | ❌ Missing | Captures 5-8% abandoning visitors | Add lightweight Alpine.js popup |
| Sticky nav CTA | ❌ Missing | 23% more CTA clicks on mobile | Add sticky "Book Free Session" button |
| Video explainer | ❌ Missing | 80% prefer video for complex services | Add Loom embed or animated explainer |

#### C. Accessibility (WCAG 2.1 AA)
- [ ] All images need `alt` attributes
- [ ] Form labels must be explicit (not placeholder-only)
- [ ] Focus states must be visible (outline on Tab navigation)
- [ ] Colour contrast ratio ≥ 4.5:1 for all text

#### D. SEO Technical Improvements
- [ ] Add `canonical` tags on all pages
- [ ] Blog posts need `article` schema markup
- [ ] Image alt text = keyword-rich descriptions
- [ ] Internal linking: each blog post links to 2–3 related posts
- [ ] `next`/`prev` pagination tags for blog index

#### E. Mobile UX (Priority — 70%+ SA traffic is mobile)
- [ ] Hamburger nav menu needs aria-label
- [ ] CTA buttons minimum 44×44px touch target
- [ ] Pricing table: horizontal scroll or card stack on mobile
- [ ] Font size minimum 16px for body text

---

## 9. Backend Dashboard Plan — AI Source Recommendation Engine

### Vision
A private dashboard where you (and clients) can upload business documents, SOPs, spreadsheets, emails, and process descriptions — and the system returns a prioritised list of AI tools/implementations to streamline each process, with estimated ROI and implementation difficulty.

### Architecture Overview

```
┌──────────────────────────────────────────────────────┐
│                  FRONTEND (React + Vite)              │
│  Upload UI │ Document List │ AI Recommendations Panel │
└────────────────────────┬─────────────────────────────┘
                         │ REST API calls
┌────────────────────────▼─────────────────────────────┐
│                FastAPI Backend (Python)               │
│  /upload  │  /analyse  │  /recommendations  │  /auth  │
└────────────────────────┬─────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
    ┌─────▼─────┐  ┌─────▼─────┐  ┌───▼────────┐
    │  File     │  │  Claude   │  │  Database  │
    │  Parser   │  │  API      │  │  (SQLite → │
    │  (PyMuPDF │  │  (Haiku   │  │  Postgres) │
    │  /docx2txt│  │  for cost)│  │            │
    └───────────┘  └───────────┘  └────────────┘
```

### Phase 1: MVP (Weeks 1–6)

**Tech Stack:**
- Frontend: React + Vite + TailwindCSS (no build complexity)
- Backend: FastAPI (Python) — same language as existing server.py
- AI: Claude Haiku via Anthropic SDK (cost-efficient, fast)
- File parsing: PyMuPDF (PDF), python-docx (Word), openpyxl (Excel)
- Storage: Local filesystem (MVP) → S3 (Phase 2)
- DB: SQLite (MVP) → PostgreSQL (Phase 2)
- Auth: Simple token-based (JWT) — single user dashboard

**MVP Features:**
1. Login page (username/password)
2. File upload (PDF, DOCX, XLSX, TXT, CSV)
3. Document library (list of uploaded files)
4. "Analyse" button → sends to Claude API
5. Results panel with:
   - Process summary (what the document describes)
   - AI recommendations (which AI tool/type to use)
   - Estimated ROI
   - Implementation difficulty (Low/Medium/High)
   - Next action (book consultation CTA)
6. Export results as PDF

**Claude Prompt Architecture:**
```
System: You are an AI implementation consultant. 
Analyse the uploaded business document and identify:
1. All manual, repetitive, or time-intensive processes
2. For each process: recommend the most appropriate AI solution
3. Include: tool name/type, estimated time savings, cost estimate, 
   implementation difficulty (1-5), and priority ranking
4. Format response as structured JSON for UI rendering
Output format: { processes: [ { name, description, aiSolution, 
  toolType, timeSavedHours, costEstimateZAR, difficulty, priority } ] }
```

**Recommended AI Tool Categories (System Knowledge Base):**
| Business Problem | AI Solution Type | Example Tools |
|----------------|-----------------|--------------|
| Customer queries | Conversational AI / Chatbot | Claude, ChatGPT API, Rasa |
| Document processing | Document AI | AWS Textract, Google DocAI, Claude |
| Email triage | NLP classification | GPT-4o, Claude Haiku |
| Invoice/finance | OCR + extraction | AWS Textract, ABBYY |
| Scheduling | Agentic AI | Claude + calendar APIs |
| Content creation | Generative AI | Claude, GPT-4o, Gemini |
| Data analysis | Analytics AI | Julius AI, Noteable |
| Image/video | Computer vision | Google Vision, AWS Rekognition |
| Quality control | Computer vision | Roboflow, AWS Lookout |
| Predictive analytics | ML/forecasting | BigML, DataRobot |
| HR/recruitment | Screening AI | HireVue, Workday AI |
| Code automation | Code AI | GitHub Copilot, Claude Code |

### Phase 2: Beta (Weeks 7–10)
- Multi-client support (user accounts per client)
- Project history and versioning
- PDF report generation with branding
- Email notifications when analysis complete
- Integration: Calendly booking link in report CTA

### Phase 3: Launch (Weeks 11–12)
- Hosted on Render.com or Railway (free tier → paid as needed)
- White-label option for resellers
- Webhook to notify your CRM when report generated
- Client portal URL per account

### File Structure
```
dashboard/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadZone.jsx
│   │   │   ├── DocumentList.jsx
│   │   │   ├── RecommendationsPanel.jsx
│   │   │   └── ExportButton.jsx
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   └── Report.jsx
│   │   └── App.jsx
│   ├── package.json
│   └── vite.config.js
├── backend/
│   ├── main.py              # FastAPI app
│   ├── routers/
│   │   ├── upload.py
│   │   ├── analyse.py
│   │   └── auth.py
│   ├── services/
│   │   ├── parser.py        # File parsing
│   │   ├── claude_client.py # Claude API calls
│   │   └── recommender.py   # Rule + AI hybrid
│   ├── models.py            # SQLAlchemy models
│   ├── database.py
│   └── requirements.txt
└── README.md
```

### Estimated Build Cost (Solo Developer)
| Phase | Hours | If outsourced (R450/hr) | DIY Cost |
|-------|-------|------------------------|---------|
| MVP | 40h | R18,000 | R0 + Claude API ~R200/month |
| Beta | 20h | R9,000 | R0 |
| Launch | 10h | R4,500 | R0 + hosting ~R150/month |

---

## 10. Verification Plan

| Deliverable | Verification Method | Pass Criterion |
|---|---|---|
| 30 blog posts live | `astro build` — count generated HTML files | 30+ posts in `/dist/blog/` |
| GitHub repo live | Access `github.com/YOUR_USERNAME/business-simplifier` | Repo is public, green Actions checkmark |
| Custom domain live | Browse to domain; check SSL | HTTPS works, no cert warning |
| GoDaddy DNS | `dig businesssimplifier.co.za A` | Returns GitHub IPs (185.199.x.x) |
| UI/UX pass | PageSpeed Insights on live URL | CWV all green |
| Content calendar | Manually check all 30 posts render | Each post has title, content, meta |
| Dashboard plan | Review Section 9 completeness | Tech stack, phases, API prompt, file structure documented |

---

*Strategy managed by: Business Simplifier Team*
*Next review: Day 15 (mid-sprint check-in)*
