"""
crawler.py — Website crawling and tech stack detection.

Runs entirely server-side using Python httpx.
No external APIs, no CORS proxy, no BuiltWith.
Detects: CMS, ecommerce, CRM, accounting, booking, analytics, email, chat, and
         any other recognisable platform from HTML source, HTTP headers, and
         meta tags — giving us a real picture of what the business already runs.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from urllib.parse import urljoin, urlparse

import httpx


# ---------------------------------------------------------------------------
# Tech fingerprints — ordered by confidence
# Each entry: (category, name, detection_fn)
# ---------------------------------------------------------------------------

def _has(pattern: str, flags: int = re.IGNORECASE):
    """Return a detector function that searches HTML for a regex pattern."""
    compiled = re.compile(pattern, flags)
    return lambda html, headers: bool(compiled.search(html))

def _header(key: str, value_pattern: str):
    """Return a detector that checks an HTTP response header."""
    compiled = re.compile(value_pattern, re.IGNORECASE)
    return lambda html, headers: bool(compiled.search(headers.get(key, "")))

def _either(fn1, fn2):
    return lambda html, headers: fn1(html, headers) or fn2(html, headers)


TECH_FINGERPRINTS: list[tuple[str, str, object]] = [
    # ── CMS ──────────────────────────────────────────────────────────────────
    ("CMS",        "WordPress",       _either(_has(r'/wp-content/|/wp-includes/|wp-json'), _header("x-powered-by", "wordpress"))),
    ("CMS",        "Wix",             _has(r'wix\.com/|wixstatic\.com|_wix_')),
    ("CMS",        "Squarespace",     _has(r'squarespace\.com|static1\.squarespace')),
    ("CMS",        "Webflow",         _has(r'webflow\.com|\.webflow\.')),
    ("CMS",        "Ghost",           _has(r'ghost\.org|ghost/api|ghostcdn')),
    ("CMS",        "Joomla",          _has(r'/components/com_|joomla')),
    ("CMS",        "Drupal",          _either(_has(r'drupal\.js|drupal\.settings'), _header("x-generator", "drupal"))),
    ("CMS",        "Shopify",         _has(r'cdn\.shopify\.com|shopifycdn\.com|Shopify\.theme')),
    ("CMS",        "WooCommerce",     _has(r'woocommerce|wc-ajax|wc_cart_fragments')),
    ("CMS",        "Magento",         _has(r'mage/|Magento_|magento')),
    ("CMS",        "PrestaShop",      _has(r'prestashop|presta-shop')),
    ("CMS",        "OpenCart",        _has(r'opencart|catalog/view/theme')),

    # ── Booking / Scheduling ─────────────────────────────────────────────────
    ("Booking",    "Calendly",        _has(r'calendly\.com')),
    ("Booking",    "Acuity",          _has(r'acuityscheduling\.com')),
    ("Booking",    "SimplyBook",      _has(r'simplybook\.me|simplybook\.it')),
    ("Booking",    "Appointlet",      _has(r'appointlet\.com')),
    ("Booking",    "Dineplan",        _has(r'dineplan\.com')),
    ("Booking",    "ResOS",           _has(r'resos\.com')),

    # ── CRM ──────────────────────────────────────────────────────────────────
    ("CRM",        "HubSpot",         _has(r'hubspot\.com|hs-scripts|hubspotforms')),
    ("CRM",        "Salesforce",      _has(r'salesforce\.com|force\.com|pardot')),
    ("CRM",        "Zoho CRM",        _has(r'zoho\.com|crm\.zoho')),
    ("CRM",        "Pipedrive",       _has(r'pipedrive\.com')),
    ("CRM",        "Freshdesk",       _has(r'freshdesk\.com|freshworks\.com')),

    # ── Accounting / Finance ─────────────────────────────────────────────────
    ("Accounting", "Xero",            _has(r'xero\.com')),
    ("Accounting", "Sage",            _has(r'sage\.com|sageone\.com')),
    ("Accounting", "QuickBooks",      _has(r'quickbooks\.com|intuit\.com')),
    ("Accounting", "FreshBooks",      _has(r'freshbooks\.com')),

    # ── Email Marketing ──────────────────────────────────────────────────────
    ("Email",      "Mailchimp",       _has(r'mailchimp\.com|mc\.us\d+\.list-manage')),
    ("Email",      "Brevo",           _has(r'sibforms\.com|brevo\.com|sendinblue')),
    ("Email",      "Klaviyo",         _has(r'klaviyo\.com')),
    ("Email",      "ActiveCampaign",  _has(r'activecampaign\.com')),
    ("Email",      "ConvertKit",      _has(r'convertkit\.com')),

    # ── Live Chat / Support ──────────────────────────────────────────────────
    ("Chat",       "Intercom",        _has(r'intercom\.io|intercomcdn')),
    ("Chat",       "Zendesk",         _has(r'zendesk\.com|zdassets\.com')),
    ("Chat",       "Tidio",           _has(r'tidio\.com|tidiochat')),
    ("Chat",       "Crisp",           _has(r'crisp\.chat')),
    ("Chat",       "Tawk.to",         _has(r'tawk\.to')),
    ("Chat",       "WhatsApp Widget", _has(r'wa\.me/|whatsapp\.com/send|api\.whatsapp')),

    # ── Analytics ────────────────────────────────────────────────────────────
    ("Analytics",  "Google Analytics",_has(r'google-analytics\.com|gtag\(|ua-\d+-\d+')),
    ("Analytics",  "Google Tag Manager",_has(r'googletagmanager\.com|GTM-')),
    ("Analytics",  "Facebook Pixel",  _has(r'connect\.facebook\.net|fbq\(')),
    ("Analytics",  "Hotjar",          _has(r'hotjar\.com|hj\(')),
    ("Analytics",  "Mixpanel",        _has(r'mixpanel\.com')),
    ("Analytics",  "Plausible",       _has(r'plausible\.io')),

    # ── Payments ─────────────────────────────────────────────────────────────
    ("Payments",   "Stripe",          _has(r'stripe\.com|js\.stripe\.com')),
    ("Payments",   "PayFast",         _has(r'payfast\.co\.za')),
    ("Payments",   "Yoco",            _has(r'yoco\.com|yoco\.africa')),
    ("Payments",   "PayGate",         _has(r'paygate\.co\.za')),
    ("Payments",   "PayPal",          _has(r'paypal\.com|paypalobjects\.com')),
    ("Payments",   "Peach Payments",  _has(r'peachpayments\.com')),

    # ── Forms ────────────────────────────────────────────────────────────────
    ("Forms",      "Typeform",        _has(r'typeform\.com|tf-\w+')),
    ("Forms",      "JotForm",         _has(r'jotform\.com')),
    ("Forms",      "Gravity Forms",   _has(r'gravityforms\.com|gform_')),
    ("Forms",      "Formspree",       _has(r'formspree\.io')),
    ("Forms",      "Google Forms",    _has(r'docs\.google\.com/forms')),

    # ── Hosting / Infrastructure ─────────────────────────────────────────────
    ("Hosting",    "Cloudflare",      _header("cf-ray", r".+")),
    ("Hosting",    "AWS CloudFront",  _header("x-amz-cf-id", r".+")),
    ("Hosting",    "Vercel",          _header("x-vercel-id", r".+")),
    ("Hosting",    "Netlify",         _header("x-nf-request-id", r".+")),
    ("Hosting",    "GitHub Pages",    _has(r'github\.io')),

    # ── SA-Specific ──────────────────────────────────────────────────────────
    ("SA Platform","Property24",      _has(r'property24\.com')),
    ("SA Platform","Private Property",_has(r'privateproperty\.co\.za')),
    ("SA Platform","Takealot",        _has(r'takealot\.com')),
    ("SA Platform","WantItAll",       _has(r'wantitall\.co\.za')),
    ("SA Platform","Loot",            _has(r'loot\.co\.za')),
    ("SA Platform","Dineplan",        _has(r'dineplan\.com')),
]


# ---------------------------------------------------------------------------
# Industry signals — from page text
# ---------------------------------------------------------------------------

INDUSTRY_SIGNALS: list[tuple[list[str], str]] = [
    (["shop", "cart", "product", "order", "checkout", "shipping", "store", "ecommerce", "catalogue", "sku"], "E-commerce & Retail"),
    (["property", "listing", "rent", "tenant", "agent", "estate", "apartment", "house", "bedroom", "plot"], "Real Estate & Property"),
    (["patient", "clinic", "medical", "health", "doctor", "hospital", "pharmacy", "appointment", "script", "consult"], "Healthcare & Wellness"),
    (["restaurant", "menu", "table", "reservation", "food", "dining", "chef", "cuisine", "takeaway", "delivery"], "Hospitality & Tourism"),
    (["recruit", "candidate", "vacancy", "hiring", "cv", "job board", "talent", "placement", "headhunt"], "HR & Recruitment"),
    (["invoice", "accounting", "tax", "bookkeeping", "financial", "audit", "payroll", "ledger", "vat", "sars"], "Financial Services"),
    (["student", "course", "learn", "tutor", "school", "enrol", "training", "lesson", "classroom", "programme"], "Education & EdTech"),
    (["manufacture", "factory", "production", "assembly", "industrial", "machinery", "engineering", "plant"], "Manufacturing & Engineering"),
    (["logistics", "transport", "fleet", "freight", "courier", "driver", "waybill", "pod", "delivery"], "Logistics & Supply Chain"),
    (["attorney", "lawyer", "legal", "law firm", "conveyancing", "litigation", "notary", "advocate"], "Legal & Professional Services"),
    (["marketing", "advertising", "agency", "campaign", "brand", "social media", "seo", "digital", "pr"], "Media & Marketing"),
    (["ngo", "nonprofit", "charity", "donor", "beneficiary", "community", "welfare", "foundation"], "Non-profit & NGO"),
    (["construction", "building", "contractor", "site", "civil", "development", "renovation", "brickwork"], "Construction & Property Dev"),
    (["agri", "farm", "crop", "livestock", "irrigation", "grain", "harvest", "silo", "maize", "wheat"], "Agriculture & Agritech"),
    (["consult", "advise", "strategy", "solution", "professional service", "managed service"], "Professional Services"),
]


# ---------------------------------------------------------------------------
# Main crawler
# ---------------------------------------------------------------------------

@dataclass
class CrawlResult:
    url: str
    domain: str
    status_code: int
    page_text: str = ""            # visible text, stripped of HTML
    page_html: str = ""            # raw HTML (first 80KB)
    headers: dict = field(default_factory=dict)
    detected_tech: list[dict] = field(default_factory=list)  # [{"category": "CMS", "name": "WordPress"}]
    inferred_industry: str = ""
    industry_confidence: int = 0   # 0-10
    raw_links: list[str] = field(default_factory=list)
    meta_description: str = ""
    page_title: str = ""
    error: str = ""


def crawl(url: str, timeout: float = 15.0) -> CrawlResult:
    """
    Crawl a URL and return a CrawlResult with detected tech, text, and industry signals.

    Args:
        url:     Full URL to crawl (https://example.co.za)
        timeout: Request timeout in seconds

    Returns:
        CrawlResult — never raises, errors go into result.error
    """
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "")
    except Exception:
        return CrawlResult(url=url, domain="", status_code=0, error="Invalid URL")

    result = CrawlResult(url=url, domain=domain, status_code=0)

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (compatible; BusinessSimplifier-AuditBot/1.0; "
                "+https://businesssimplifier.co.za)"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-ZA,en;q=0.9",
        }

        with httpx.Client(
            timeout=timeout,
            follow_redirects=True,
            headers=headers,
        ) as client:
            resp = client.get(url)

        result.status_code = resp.status_code
        result.headers = dict(resp.headers)

        html = resp.text[:80_000]  # Cap at 80KB to keep processing fast
        result.page_html = html

        # ── Extract visible text ─────────────────────────────────────────────
        text = html
        text = re.sub(r"<style[^>]*>[\s\S]*?</style>", " ", text, flags=re.IGNORECASE)
        text = re.sub(r"<script[^>]*>[\s\S]*?</script>", " ", text, flags=re.IGNORECASE)
        text = re.sub(r"<!--[\s\S]*?-->", " ", text)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        result.page_text = text[:6000].lower()  # First 6000 chars, lowercased

        # ── Extract page title ───────────────────────────────────────────────
        title_match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        if title_match:
            result.page_title = re.sub(r"\s+", " ", title_match.group(1)).strip()

        # ── Extract meta description ─────────────────────────────────────────
        meta_match = re.search(
            r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']',
            html, re.IGNORECASE
        )
        if meta_match:
            result.meta_description = meta_match.group(1).strip()

        # ── Extract internal links ───────────────────────────────────────────
        links = re.findall(r'href=["\']([^"\'#?]+)["\']', html, re.IGNORECASE)
        base = f"{parsed.scheme}://{parsed.netloc}"
        internal = []
        for link in links:
            if link.startswith("/") and not link.startswith("//"):
                internal.append(urljoin(base, link))
            elif domain in link:
                internal.append(link)
        result.raw_links = list(set(internal))[:20]

    except httpx.TimeoutException:
        result.error = f"Request timed out after {timeout}s"
        return result
    except httpx.ConnectError as e:
        result.error = f"Could not connect: {e}"
        return result
    except Exception as e:
        result.error = f"Unexpected error: {e}"
        return result

    # ── Tech detection ───────────────────────────────────────────────────────
    result.detected_tech = detect_tech(result.page_html, result.headers)

    # ── Industry inference ───────────────────────────────────────────────────
    result.inferred_industry, result.industry_confidence = infer_industry(
        result.page_text, result.page_title, result.meta_description
    )

    return result


def detect_tech(html: str, headers: dict) -> list[dict]:
    """
    Run all tech fingerprints against HTML and response headers.

    Returns:
        List of {"category": str, "name": str} dicts, deduplicated.
    """
    found = []
    seen_names: set[str] = set()

    for category, name, detector in TECH_FINGERPRINTS:
        if name not in seen_names and detector(html, headers):
            found.append({"category": category, "name": name})
            seen_names.add(name)

    return found


def infer_industry(text: str, title: str, meta: str) -> tuple[str, int]:
    """
    Infer the most likely industry from page text, title, and meta description.

    Returns:
        (industry_name, confidence_score_0_to_10)
    """
    combined = f"{title} {meta} {text}".lower()
    best_industry = ""
    best_score = 0

    for keywords, industry in INDUSTRY_SIGNALS:
        score = sum(1 for kw in keywords if kw in combined)
        if score > best_score:
            best_score = score
            best_industry = industry

    # Normalise confidence: 2 keywords = 3, 5+ = 8, 8+ = 10
    confidence = min(10, int(best_score * 1.5))
    if best_score < 2:
        best_industry = ""
        confidence = 0

    return best_industry, confidence
