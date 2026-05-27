"""
automation_map.py — Master automation opportunity database.

This is the intelligence core. For every detected tech stack signal, industry,
and pain point keyword, it maps to a specific automation opportunity with:
  - What it is
  - What to build (using our lib/ stack or a free tool)
  - ZAR cost estimate to implement
  - Time saved per month
  - Payback period in weeks
  - Difficulty
  - Which of our 13 coded demos it maps to (if applicable)
  - Whether it can be built with our existing stack (no paid tools needed)

This is the internal version — it suggests ALL possibilities, including both
our custom-built solutions and free/low-cost external tools where they genuinely
outperform a custom build.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AutomationOpportunity:
    id: str                          # Unique slug, e.g. "whatsapp-customer-service"
    title: str
    category: str                    # e.g. "Customer Communication", "Document Automation"
    description: str
    build_approach: str              # "custom" | "free-tool" | "hybrid"
    custom_build_detail: str         # How we'd build it with our stack
    free_tool_alternative: str       # Best free/cheap tool if not building custom
    monthly_time_saved_hrs: int
    setup_cost_zar: int              # One-off build cost in ZAR
    monthly_cost_zar: int            # Ongoing monthly cost in ZAR
    payback_weeks: int
    difficulty: str                  # "Low" | "Medium" | "High"
    demo_id: str = ""                # e.g. "I02" — links to our coded demo
    demo_label: str = ""             # Human label for the demo
    trigger_tech: list[str] = field(default_factory=list)    # Tech that makes this extra relevant
    trigger_keywords: list[str] = field(default_factory=list) # Pain keywords
    trigger_industries: list[str] = field(default_factory=list)
    priority_score: int = 5          # 1–10, used for ranking


# ---------------------------------------------------------------------------
# MASTER AUTOMATION CATALOGUE
# ---------------------------------------------------------------------------

AUTOMATIONS: list[AutomationOpportunity] = [

    # ── CUSTOMER COMMUNICATION ──────────────────────────────────────────────

    AutomationOpportunity(
        id="whatsapp-faq-bot",
        title="WhatsApp 24/7 FAQ & Query Bot",
        category="Customer Communication",
        description=(
            "An AI chatbot that handles your most common customer questions via WhatsApp around the clock — "
            "product queries, pricing, hours, availability, and FAQs — without any staff involvement. "
            "Resolves 60–70% of inbound WhatsApp messages automatically."
        ),
        build_approach="custom",
        custom_build_detail=(
            "Built with lib/whatsapp.py (webhook handler) + lib/llm.py (response generation) + "
            "lib/db.py (FAQ SQLite store). Deployed as a FastAPI service. "
            "Estimated build time: 1–2 days."
        ),
        free_tool_alternative="WhatsApp Business App (manual auto-replies only, very limited)",
        monthly_time_saved_hrs=20,
        setup_cost_zar=4500,
        monthly_cost_zar=350,
        payback_weeks=5,
        difficulty="Low",
        demo_id="I01",
        demo_label="Retail WhatsApp Inventory Bot",
        trigger_tech=["WhatsApp Widget"],
        trigger_keywords=["whatsapp", "chat", "message", "query", "enquiry", "faq", "24/7"],
        trigger_industries=["E-commerce & Retail", "Healthcare & Wellness", "Hospitality & Tourism",
                            "Real Estate & Property", "Education & EdTech", "Legal & Professional Services"],
        priority_score=9,
    ),

    AutomationOpportunity(
        id="whatsapp-booking-bot",
        title="WhatsApp Appointment Booking Bot",
        category="Customer Communication",
        description=(
            "A multi-turn WhatsApp bot that guides customers through booking an appointment or reservation — "
            "collects their details, checks availability in real time, confirms the slot, and sends a reminder "
            "24 hours before. No phone calls, no back-and-forth, no double-bookings."
        ),
        build_approach="custom",
        custom_build_detail=(
            "Built with lib/whatsapp.py state machine + lib/db.py (SQLite calendar store) + "
            "lib/emailer.py (confirmation email). "
            "Demo I02 is a working implementation for healthcare — adaptable to any industry."
        ),
        free_tool_alternative="Calendly free plan (web only, not WhatsApp-native)",
        monthly_time_saved_hrs=18,
        setup_cost_zar=5500,
        monthly_cost_zar=400,
        payback_weeks=6,
        difficulty="Low",
        demo_id="I02",
        demo_label="Healthcare WhatsApp Booking Bot",
        trigger_tech=["Calendly", "Acuity", "SimplyBook", "WhatsApp Widget"],
        trigger_keywords=["booking", "appointment", "schedule", "availability", "reservation", "no-show"],
        trigger_industries=["Healthcare & Wellness", "Hospitality & Tourism", "Legal & Professional Services",
                            "Education & EdTech", "Professional Services"],
        priority_score=8,
    ),

    AutomationOpportunity(
        id="whatsapp-order-status-bot",
        title="WhatsApp Order & Shipment Status Bot",
        category="Customer Communication",
        description=(
            "Customers send their order or tracking number via WhatsApp and instantly receive a status update "
            "from your system. Eliminates the #1 cause of inbound support volume: 'Where is my order?'"
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/whatsapp.py + lib/db.py (shipment/order SQLite store synced from your system) + "
            "lib/llm.py (natural language formatting). Demo I09 covers logistics; Demo I01 covers retail orders."
        ),
        free_tool_alternative="Manual replies — no free tool does this without integration work",
        monthly_time_saved_hrs=15,
        setup_cost_zar=4800,
        monthly_cost_zar=300,
        payback_weeks=5,
        difficulty="Low",
        demo_id="I09",
        demo_label="Logistics Shipment Tracker Bot",
        trigger_tech=["WooCommerce", "Shopify", "WhatsApp Widget"],
        trigger_keywords=["order", "tracking", "shipment", "delivery", "status", "dispatch"],
        trigger_industries=["E-commerce & Retail", "Logistics & Supply Chain", "Manufacturing & Engineering"],
        priority_score=8,
    ),

    AutomationOpportunity(
        id="whatsapp-property-search",
        title="WhatsApp Property Search Bot",
        category="Customer Communication",
        description=(
            "Buyers and renters describe what they're looking for via WhatsApp in plain language — "
            "'3-bed house in Stellenbosch under R2m' — and the bot searches your listings database and "
            "returns the top matches with details and photos. Agents focus on hot leads, not search queries."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/whatsapp.py + lib/llm.py (natural language to search query parsing) + "
            "lib/db.py (listings SQLite). Demo I04 is the full implementation."
        ),
        free_tool_alternative="Property24 / Private Property (external, you lose the lead data)",
        monthly_time_saved_hrs=25,
        setup_cost_zar=6500,
        monthly_cost_zar=450,
        payback_weeks=5,
        difficulty="Medium",
        demo_id="I04",
        demo_label="Real Estate Property Search Bot",
        trigger_tech=["WhatsApp Widget", "Property24", "Private Property"],
        trigger_keywords=["property", "listing", "bedroom", "rent", "buy", "estate", "agent"],
        trigger_industries=["Real Estate & Property"],
        priority_score=9,
    ),

    AutomationOpportunity(
        id="construction-client-updates",
        title="Site Progress WhatsApp Broadcast",
        category="Customer Communication",
        description=(
            "Site managers submit a daily progress update via a simple form. An AI formats it into a "
            "professional client message and broadcasts it to all project stakeholders on WhatsApp. "
            "Clients stay informed, managers save 1+ hour/day."
        ),
        build_approach="custom",
        custom_build_detail=(
            "FastAPI form endpoint + lib/llm.py (format the update professionally) + "
            "lib/whatsapp.py (broadcast to contact list). Demo I13 is the full implementation."
        ),
        free_tool_alternative="WhatsApp group chats (manual, no formatting, no tracking)",
        monthly_time_saved_hrs=22,
        setup_cost_zar=4200,
        monthly_cost_zar=300,
        payback_weeks=5,
        difficulty="Low",
        demo_id="I13",
        demo_label="Construction Site Update Broadcaster",
        trigger_tech=["WhatsApp Widget"],
        trigger_keywords=["construction", "site", "project", "client update", "progress", "milestone"],
        trigger_industries=["Construction & Property Dev"],
        priority_score=8,
    ),

    # ── DOCUMENT & PROCESS AUTOMATION ──────────────────────────────────────

    AutomationOpportunity(
        id="ai-document-drafting",
        title="AI Contract & Document Drafting",
        category="Document Automation",
        description=(
            "Generate first drafts of standard contracts, engagement letters, NDAs, scope of work documents, "
            "and proposals from a structured intake form. What takes 45–90 minutes takes under 5 minutes. "
            "Staff review and finalise — AI does the boilerplate."
        ),
        build_approach="custom",
        custom_build_detail=(
            "FastAPI intake form + lib/llm.py with document-specific prompt templates + "
            "lib/emailer.py to deliver the draft. Demo I06 covers legal intake specifically."
        ),
        free_tool_alternative="Claude.ai / ChatGPT free tier (manual prompt each time, no workflow)",
        monthly_time_saved_hrs=24,
        setup_cost_zar=6500,
        monthly_cost_zar=400,
        payback_weeks=5,
        difficulty="Medium",
        demo_id="I06",
        demo_label="Legal Client Intake & Document Generator",
        trigger_tech=["WordPress", "Typeform", "JotForm", "Google Forms"],
        trigger_keywords=["contract", "document", "proposal", "nda", "letter", "draft", "agreement", "scope"],
        trigger_industries=["Legal & Professional Services", "Professional Services",
                            "HR & Recruitment", "Construction & Property Dev"],
        priority_score=8,
    ),

    AutomationOpportunity(
        id="client-intake-automation",
        title="Automated Client Intake & Onboarding",
        category="Document Automation",
        description=(
            "Replace manual intake forms with a digital flow that collects client information, validates it, "
            "stores it in your system, and triggers the next step automatically — welcome email, document checklist, "
            "calendar invite — without any staff manually processing the submission."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/forms.py (FastAPI + Pydantic validation) + lib/db.py (SQLite store) + "
            "lib/emailer.py (automated welcome email + document checklist)."
        ),
        free_tool_alternative="Google Forms + Gmail (basic, no automation, no integration)",
        monthly_time_saved_hrs=16,
        setup_cost_zar=4800,
        monthly_cost_zar=300,
        payback_weeks=6,
        difficulty="Low",
        demo_id="I06",
        demo_label="Legal Client Intake & Document Generator",
        trigger_tech=["Typeform", "JotForm", "Google Forms", "Gravity Forms", "Formspree"],
        trigger_keywords=["intake", "onboard", "new client", "registration", "sign up", "application"],
        trigger_industries=["Legal & Professional Services", "Healthcare & Wellness",
                            "Financial Services", "Education & EdTech", "Professional Services"],
        priority_score=7,
    ),

    AutomationOpportunity(
        id="lead-scoring-qualification",
        title="Automated Lead Scoring & Qualification",
        category="Sales Automation",
        description=(
            "Incoming leads from your website forms are automatically scored based on budget, industry, "
            "team size, and stated need. Hot leads are flagged immediately; low-quality leads get a "
            "nurture sequence. Your sales team only speaks to people worth their time."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/forms.py (lead capture endpoint) + lib/llm.py (qualification scoring) + "
            "lib/emailer.py (instant lead notification to sales) + lib/db.py (lead pipeline store). "
            "Demo I03 covers financial services lead scoring."
        ),
        free_tool_alternative="HubSpot CRM free plan (manual scoring, no AI)",
        monthly_time_saved_hrs=20,
        setup_cost_zar=5500,
        monthly_cost_zar=350,
        payback_weeks=5,
        difficulty="Medium",
        demo_id="I03",
        demo_label="Financial Services Lead Scoring Script",
        trigger_tech=["HubSpot", "Salesforce", "Zoho CRM", "Gravity Forms", "Typeform"],
        trigger_keywords=["lead", "qualification", "prospect", "pipeline", "sales", "crm", "follow-up"],
        trigger_industries=["Financial Services", "Real Estate & Property", "HR & Recruitment",
                            "Professional Services", "Legal & Professional Services"],
        priority_score=8,
    ),

    # ── CONTENT & MARKETING AUTOMATION ─────────────────────────────────────

    AutomationOpportunity(
        id="ai-content-engine",
        title="AI Content Generation Engine",
        category="Content & Marketing",
        description=(
            "A scheduled pipeline that reads your content calendar and generates blog posts, LinkedIn articles, "
            "social media captions, and email newsletters automatically. One content calendar drives all your "
            "channels without a writer for every piece."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/content.py + lib/llm.py + lib/scheduler.py. The content-engine/ directory in our repo "
            "is a working implementation — calendar.csv → LLM → Markdown files → published automatically."
        ),
        free_tool_alternative="ChatGPT / Claude.ai (manual prompting, no scheduling, no pipeline)",
        monthly_time_saved_hrs=28,
        setup_cost_zar=4200,
        monthly_cost_zar=300,
        payback_weeks=4,
        difficulty="Low",
        demo_id="I11",
        demo_label="Media Content Scheduler",
        trigger_tech=["WordPress", "Ghost", "Mailchimp", "Brevo", "Google Analytics"],
        trigger_keywords=["content", "blog", "social", "post", "article", "linkedin", "newsletter", "copy"],
        trigger_industries=["Media & Marketing", "Professional Services", "Education & EdTech",
                            "E-commerce & Retail", "Non-profit & NGO"],
        priority_score=7,
    ),

    AutomationOpportunity(
        id="upsell-follow-up-automation",
        title="Post-Purchase Upsell & Follow-Up Automation",
        category="Content & Marketing",
        description=(
            "Timed email sequences triggered by a purchase, booking, or check-in. "
            "Day 2: personalised upsell offer. Day 7: review request. Day 30: re-engagement offer. "
            "All personalised by the customer's actual purchase/booking using AI."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/emailer.py + lib/scheduler.py + lib/llm.py (personalise each email body) + "
            "lib/db.py (trigger tracking). Demo I05 covers hospitality upsells specifically."
        ),
        free_tool_alternative="Mailchimp free tier (3 emails max per automation, limited personalisation)",
        monthly_time_saved_hrs=12,
        setup_cost_zar=4500,
        monthly_cost_zar=350,
        payback_weeks=5,
        difficulty="Low",
        demo_id="I05",
        demo_label="Hospitality Booking + Follow-up Automation",
        trigger_tech=["Mailchimp", "Klaviyo", "WooCommerce", "Shopify"],
        trigger_keywords=["upsell", "follow-up", "retention", "review", "repeat", "email sequence", "nurture"],
        trigger_industries=["Hospitality & Tourism", "E-commerce & Retail", "Healthcare & Wellness",
                            "Education & EdTech"],
        priority_score=7,
    ),

    AutomationOpportunity(
        id="donor-acknowledgement-pipeline",
        title="Personalised Donor/Member Acknowledgement Pipeline",
        category="Content & Marketing",
        description=(
            "Every new donation, membership renewal, or contribution triggers a personalised thank-you email "
            "generated by AI — referencing their specific contribution, its impact, and next steps. "
            "No template that reads like a template."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/llm.py (personalised email body) + lib/emailer.py + lib/db.py (sent tracking). "
            "Demo I12 is a complete implementation for NGOs — adaptable to any membership organisation."
        ),
        free_tool_alternative="Mailchimp free (500 contacts, generic templates, no AI personalisation)",
        monthly_time_saved_hrs=14,
        setup_cost_zar=3800,
        monthly_cost_zar=250,
        payback_weeks=4,
        difficulty="Low",
        demo_id="I12",
        demo_label="NGO Donor Acknowledgement Pipeline",
        trigger_tech=["Mailchimp", "Brevo", "PayFast", "PayGate"],
        trigger_keywords=["donor", "donation", "member", "thank you", "acknowledgement", "contribution"],
        trigger_industries=["Non-profit & NGO", "Education & EdTech"],
        priority_score=6,
    ),

    # ── ANALYTICS & REPORTING ───────────────────────────────────────────────

    AutomationOpportunity(
        id="automated-reporting-dashboard",
        title="Automated Business Performance Dashboard",
        category="Analytics & Reporting",
        description=(
            "A live dashboard that pulls data from your existing tools and shows revenue, leads, "
            "conversion rates, and key KPIs in one place. Weekly email digest sent automatically to "
            "management. No more manually compiling spreadsheet reports."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/analytics.py + FastAPI dashboard endpoint + lib/emailer.py (weekly digest) + "
            "lib/scheduler.py (auto-send). Stores all events in SQLite — fully owned data."
        ),
        free_tool_alternative="Google Looker Studio (free, but requires manual setup per data source)",
        monthly_time_saved_hrs=16,
        setup_cost_zar=6000,
        monthly_cost_zar=400,
        payback_weeks=7,
        difficulty="Medium",
        demo_id="",
        demo_label="",
        trigger_tech=["Google Analytics", "Google Tag Manager", "HubSpot", "Shopify",
                      "WooCommerce", "Xero", "Sage"],
        trigger_keywords=["report", "dashboard", "analytics", "metrics", "kpi", "performance",
                          "insights", "forecast"],
        trigger_industries=["Financial Services", "E-commerce & Retail", "Professional Services",
                            "Manufacturing & Engineering", "Logistics & Supply Chain"],
        priority_score=7,
    ),

    AutomationOpportunity(
        id="agriculture-alerts",
        title="Automated Commodity Price & Weather Alert System",
        category="Analytics & Reporting",
        description=(
            "A scheduled script that fetches live weather forecasts and commodity prices from free "
            "public APIs, then sends a personalised WhatsApp digest to your farmer/client contact list "
            "each morning. Actionable intelligence delivered automatically."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/scheduler.py + Open-Meteo free API (no key needed) + lib/whatsapp.py broadcast + "
            "lib/llm.py (format the alert in plain language). Demo I08 is a complete implementation."
        ),
        free_tool_alternative="Manual WhatsApp messages (daily, takes 30–60 mins per day)",
        monthly_time_saved_hrs=20,
        setup_cost_zar=3500,
        monthly_cost_zar=250,
        payback_weeks=4,
        difficulty="Low",
        demo_id="I08",
        demo_label="Agriculture Weather & Price Alert Script",
        trigger_tech=["WhatsApp Widget"],
        trigger_keywords=["weather", "commodity", "price", "forecast", "farm", "crop", "grain", "maize"],
        trigger_industries=["Agriculture & Agritech"],
        priority_score=8,
    ),

    AutomationOpportunity(
        id="maintenance-scheduler",
        title="Predictive Maintenance Alert System",
        category="Analytics & Reporting",
        description=(
            "Reads your asset register (machinery, vehicles, equipment) and automatically calculates "
            "what maintenance is due in the next 7–14 days. Sends a prioritised maintenance schedule "
            "to the facilities manager every Monday morning. Prevents costly unplanned downtime."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/scheduler.py + lib/llm.py (generate the schedule report) + lib/emailer.py. "
            "CSV or SQLite asset register — no specialist software needed. Demo I10 is a full implementation."
        ),
        free_tool_alternative="Spreadsheet with manual due-date calculations (error-prone, easily missed)",
        monthly_time_saved_hrs=18,
        setup_cost_zar=4000,
        monthly_cost_zar=280,
        payback_weeks=5,
        difficulty="Low",
        demo_id="I10",
        demo_label="Manufacturing Maintenance Scheduler",
        trigger_tech=[],
        trigger_keywords=["maintenance", "machine", "asset", "downtime", "service", "repair", "equipment"],
        trigger_industries=["Manufacturing & Engineering", "Logistics & Supply Chain",
                            "Construction & Property Dev"],
        priority_score=7,
    ),

    # ── ECOMMERCE SPECIFIC ──────────────────────────────────────────────────

    AutomationOpportunity(
        id="ai-product-descriptions",
        title="AI Product Description & SEO Copy Generator",
        category="Content & Marketing",
        description=(
            "Generate SEO-optimised product descriptions, meta titles, and ad copy from a product name "
            "and a few bullet points. Scale your catalogue to 1,000 products without scaling your team. "
            "Consistent tone, consistent quality, fraction of the cost."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/content.py + lib/llm.py with a product-specific prompt template. "
            "Reads a CSV of products, outputs descriptions in bulk. Integrates with Shopify/WooCommerce via CSV import."
        ),
        free_tool_alternative="ChatGPT / Claude.ai free (manual, one at a time, no bulk processing)",
        monthly_time_saved_hrs=20,
        setup_cost_zar=3200,
        monthly_cost_zar=250,
        payback_weeks=4,
        difficulty="Low",
        demo_id="I11",
        demo_label="Media Content Scheduler",
        trigger_tech=["Shopify", "WooCommerce", "Magento", "PrestaShop", "OpenCart"],
        trigger_keywords=["product", "description", "catalogue", "sku", "seo", "copy", "listing"],
        trigger_industries=["E-commerce & Retail"],
        priority_score=7,
    ),

    AutomationOpportunity(
        id="inventory-reorder-alerts",
        title="Automated Inventory Reorder Alerts",
        category="Process Automation",
        description=(
            "Monitor stock levels against minimum thresholds and automatically send reorder alerts "
            "to your procurement team or supplier via email or WhatsApp. Never stockout because "
            "someone forgot to check the storeroom."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/scheduler.py + lib/db.py (stock level store) + lib/emailer.py / lib/whatsapp.py "
            "(reorder alert). Reads stock data from CSV export or direct database connection."
        ),
        free_tool_alternative="Spreadsheet with manual monitoring (easily missed, no automated alerts)",
        monthly_time_saved_hrs=10,
        setup_cost_zar=3500,
        monthly_cost_zar=220,
        payback_weeks=5,
        difficulty="Low",
        demo_id="I01",
        demo_label="Retail WhatsApp Inventory Bot",
        trigger_tech=["Shopify", "WooCommerce", "Sage"],
        trigger_keywords=["stock", "inventory", "reorder", "shortage", "out of stock", "supplier"],
        trigger_industries=["E-commerce & Retail", "Manufacturing & Engineering",
                            "Hospitality & Tourism"],
        priority_score=6,
    ),

    # ── EDUCATION SPECIFIC ──────────────────────────────────────────────────

    AutomationOpportunity(
        id="education-faq-course-recommender",
        title="Education FAQ Bot & AI Course Recommender",
        category="Customer Communication",
        description=(
            "A WhatsApp bot that answers admissions FAQs instantly, then — when a student asks "
            "'what course is right for me?' — runs a 3-question profiling conversation and uses AI "
            "to recommend the best match from your catalogue with reasoning."
        ),
        build_approach="custom",
        custom_build_detail=(
            "lib/whatsapp.py state machine + lib/db.py (FAQ + course catalogue) + "
            "lib/llm.py (course recommendation engine). Demo I07 is the complete implementation."
        ),
        free_tool_alternative="Static FAQ page (no conversation, high drop-off rate)",
        monthly_time_saved_hrs=20,
        setup_cost_zar=5200,
        monthly_cost_zar=380,
        payback_weeks=6,
        difficulty="Medium",
        demo_id="I07",
        demo_label="Education FAQ Bot & Course Recommender",
        trigger_tech=["WhatsApp Widget", "Typeform"],
        trigger_keywords=["course", "programme", "enrol", "student", "admissions", "recommend", "tuition"],
        trigger_industries=["Education & EdTech"],
        priority_score=8,
    ),

    # ── FINANCE SPECIFIC ────────────────────────────────────────────────────

    AutomationOpportunity(
        id="invoice-processing-automation",
        title="Automated Invoice Capture & Processing",
        category="Process Automation",
        description=(
            "Supplier invoices arriving via email are automatically extracted, validated, and recorded "
            "in your accounting system. OCR reads the invoice; AI validates supplier name, amount, VAT, "
            "and due date; the record is created — no manual data entry at all."
        ),
        build_approach="hybrid",
        custom_build_detail=(
            "Python email watcher (IMAP) + lib/llm.py (extract fields from invoice text/PDF) + "
            "lib/db.py (invoice staging) + integration to Xero/Sage API if available."
        ),
        free_tool_alternative="Dext free trial → R890/month (worth it at volume; cheaper than staff time)",
        monthly_time_saved_hrs=22,
        setup_cost_zar=7000,
        monthly_cost_zar=500,
        payback_weeks=4,
        difficulty="Medium",
        demo_id="I03",
        demo_label="Financial Services Lead Scoring Script",
        trigger_tech=["Xero", "Sage", "QuickBooks", "FreshBooks"],
        trigger_keywords=["invoice", "accounts payable", "supplier", "vat", "bookkeeping", "data entry"],
        trigger_industries=["Financial Services", "Professional Services", "Legal & Professional Services"],
        priority_score=8,
    ),

    # ── HR SPECIFIC ─────────────────────────────────────────────────────────

    AutomationOpportunity(
        id="cv-screening-automation",
        title="AI CV Screening & Candidate Shortlisting",
        category="Process Automation",
        description=(
            "CVs received via email or a web form are automatically screened against a job brief "
            "using AI. Each CV gets a fit score and a 3-line summary. Your shortlist is ready in "
            "minutes — not the 2–3 days manual screening typically takes."
        ),
        build_approach="custom",
        custom_build_detail=(
            "Python email IMAP watcher + lib/llm.py (score + summarise CV text) + "
            "lib/emailer.py (daily shortlist digest to hiring manager) + lib/db.py (applicant tracking)."
        ),
        free_tool_alternative="Google Forms + manual review (no scoring, no ranking, slow)",
        monthly_time_saved_hrs=25,
        setup_cost_zar=5800,
        monthly_cost_zar=380,
        payback_weeks=6,
        difficulty="Medium",
        demo_id="",
        demo_label="",
        trigger_tech=["HubSpot", "Salesforce", "Gravity Forms", "Typeform"],
        trigger_keywords=["cv", "resume", "candidate", "shortlist", "screening", "hiring", "vacancy"],
        trigger_industries=["HR & Recruitment"],
        priority_score=8,
    ),
]


# ---------------------------------------------------------------------------
# Matching engine
# ---------------------------------------------------------------------------

def score_opportunity(
    opp: AutomationOpportunity,
    detected_tech_names: list[str],
    inferred_industry: str,
    pain_text: str,
    selected_industry: str,
) -> int:
    """
    Score how relevant an automation opportunity is to a specific business.

    Returns a score 0–100. Higher = more relevant.
    """
    score = opp.priority_score * 5  # Base score from priority (max 50)
    pain_lower = pain_text.lower()

    # Tech matches (+10 per matching tech)
    for tech in opp.trigger_tech:
        if tech in detected_tech_names:
            score += 10

    # Industry match (+20 if exact, +10 if similar)
    effective_industry = selected_industry or inferred_industry
    if effective_industry in opp.trigger_industries:
        score += 20
    elif any(
        part in effective_industry.lower()
        for ind in opp.trigger_industries
        for part in ind.lower().split()
        if len(part) > 4
    ):
        score += 8

    # Keyword matches (+8 per keyword found in pain description)
    for kw in opp.trigger_keywords:
        if kw in pain_lower:
            score += 8

    return score


def get_ranked_opportunities(
    detected_tech_names: list[str],
    inferred_industry: str,
    pain_text: str,
    selected_industry: str,
    top_n: int = 8,
) -> list[tuple[AutomationOpportunity, int]]:
    """
    Return top N automation opportunities ranked by relevance to this business.

    Returns:
        List of (opportunity, score) tuples, sorted descending by score.
    """
    scored = []
    for opp in AUTOMATIONS:
        s = score_opportunity(opp, detected_tech_names, inferred_industry, pain_text, selected_industry)
        scored.append((opp, s))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]
