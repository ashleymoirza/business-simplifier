/**
 * SEO utilities — structured data, meta generators, keyword helpers
 */

const SITE_CONFIG = {
  name: 'Business Simplifier',
  tagline: 'AI That Simplifies Your Business',
  description:
    'We help SMEs save R135K/year on average by streamlining processes with AI. Free 1-hour consultation. Custom AI solutions — chatbots, automation, analytics.',
  url: 'https://businesssimplifier.co.za',
  locale: 'en_ZA',
  localeAlt: 'en_US',
  twitter: '@BizSimplifier_ZA',
};

/**
 * Generate standard meta tags for any page
 * @param {{ title: string, description?: string, image?: string, slug?: string, type?: string, publishedTime?: string, author?: string }} opts
 */
export function getMetaTags(opts) {
  const { title, description = SITE_CONFIG.description, image = '/og-default.png', slug = '', type = 'website', publishedTime, author } = opts;
  const fullTitle = `${title} | ${SITE_CONFIG.name}`;
  const canonical = `${SITE_CONFIG.url}/${slug}`.replace(/\/$/, '');

  return {
    title: fullTitle,
    description,
    canonical,
    openGraph: {
      title: fullTitle,
      description,
      url: canonical,
      siteName: SITE_CONFIG.name,
      locale: SITE_CONFIG.locale,
      type,
      ...(publishedTime && { publishedTime }),
      ...(author && { author }),
    },
    twitter: {
      card: 'summary_large_image',
      title: fullTitle,
      description,
      image,
    },
  };
}

/**
 * JSON-LD Organization schema
 */
export function organizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: SITE_CONFIG.name,
    url: SITE_CONFIG.url,
    description: SITE_CONFIG.description,
    slogan: SITE_CONFIG.tagline,
    email: 'sales@businesssimplifier.co.za',
    foundingDate: '2025',
    areaServed: ['ZA', 'US', 'GB', 'AU', 'DE', 'CA'],
    knowsAbout: [
      'Artificial Intelligence',
      'Machine Learning',
      'Business Process Automation',
      'Chatbot Development',
      'Data Analytics',
    ],
    offers: [
      { '@type': 'Offer', name: 'Free 1-Hour AI Consultation', price: '0', priceCurrency: 'ZAR' },
      { '@type': 'Offer', name: 'AI Chatbot', price: '5000', priceCurrency: 'ZAR' },
      { '@type': 'Offer', name: 'Business Process Automation', price: '15000', priceCurrency: 'ZAR' },
    ],
  };
}

/**
 * JSON-LD BreadcrumbList schema
 * @param {{ name: string, slug: string }[]} items
 */
export function breadcrumbSchema(items) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: item.name,
      item: `${SITE_CONFIG.url}/${item.slug}`,
    })),
  };
}

/**
 * JSON-LD FAQ schema
 * @param {{ question: string, answer: string }[]} questions
 */
export function faqSchema(questions) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: questions.map((q) => ({
      '@type': 'Question',
      name: q.question,
      acceptedAnswer: { '@type': 'Answer', text: q.answer },
    })),
  };
}

/**
 * Comma-separated keywords for meta tag
 */
export const GLOBAL_KEYWORDS = [
  'business simplification',
  'AI consulting South Africa',
  'AI automation for small business',
  'business AI solutions',
  'AI chatbots South Africa',
  'process automation',
  'AI for SMEs',
  'affordable AI consulting',
  'AI strategy consulting',
  'cost savings AI',
  'small business AI',
].join(', ');

export default SITE_CONFIG;