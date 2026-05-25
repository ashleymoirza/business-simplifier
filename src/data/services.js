/**
 * Services data — used across service pages, pricing, and structured data
 * @typedef {{ id: string, title: string, tagline: string, description: string, icon: string, features: string[], idealFor: string, priceSA: string, priceIntl: string, cta: string }} Service
 */

/** @type {Service[]} */
const services = [
  {
    id: 'strategy',
    title: 'AI Strategy Consultation',
    tagline: 'Your roadmap to AI-powered business transformation',
    description:
      'A structured assessment of your business processes to identify high-impact AI opportunities. You get a prioritised roadmap with estimated ROI for each initiative.',
    icon: '🧭',
    features: [
      'Business process audit & opportunity mapping',
      'Competitive AI landscape analysis',
      'Custom AI adoption roadmap with ROI estimates',
      'Technology stack recommendations',
      'Implementation timeline & budget planning',
    ],
    idealFor: 'SMEs and startups unsure where to start with AI',
    priceSA: 'Free 1-hour session',
    priceIntl: 'Free 1-hour session',
    cta: 'Book Your Free Consultation',
  },
  {
    id: 'chatbot',
    title: 'AI Chatbot Development',
    tagline: 'Intelligent conversations that convert and support',
    description:
      'Custom AI chatbots for customer support, lead generation, or internal knowledge bases. Trained on your data and deployed on your website or messaging platforms.',
    icon: '🤖',
    features: [
      'Custom-trained on your business data and docs',
      'Multi-channel deployment (web, WhatsApp, Slack)',
      'Lead capture integration with your CRM',
      'Sentiment analysis & escalation routing',
      'Analytics dashboard for conversation insights',
    ],
    idealFor: 'Businesses wanting 24/7 customer engagement without hiring',
    priceSA: 'R 7,500 – R 25,000',
    priceIntl: '$500 – $2,500',
    cta: 'Build Your Chatbot',
  },
  {
    id: 'automation',
    title: 'Business Process Automation',
    tagline: 'Automate repetitive work and free your team',
    description:
      'End-to-end automation of repetitive workflows using AI. From email processing and data entry to complex multi-step approval chains.',
    icon: '⚡',
    features: [
      'Workflow mapping & automation opportunity audit',
      'AI-powered document processing & data extraction',
      'Email automation & smart routing',
      'CRM & ERP integration',
      'Reporting dashboard with ROI tracking',
    ],
    idealFor: 'Teams drowning in manual, repetitive tasks',
    priceSA: 'R 15,000 – R 50,000',
    priceIntl: '$1,500 – $5,000',
    cta: 'Automate Your Workflow',
  },
  {
    id: 'analytics',
    title: 'AI Analytics & Insights',
    tagline: 'Turn your data into actionable business intelligence',
    description:
      'Connect your data sources and get AI-powered dashboards, predictive analytics, and natural-language querying. Ask questions about your business in plain English.',
    icon: '📊',
    features: [
      'Multi-source data integration',
      'AI-powered dashboard & visualisations',
      'Natural language query interface',
      'Predictive analytics & trend forecasting',
      'Automated report generation (daily/weekly)',
    ],
    idealFor: 'Data-rich businesses lacking actionable insights',
    priceSA: 'R 10,000 – R 35,000',
    priceIntl: '$1,000 – $3,500',
    cta: 'Unlock Your Data',
  },
  {
    id: 'content',
    title: 'AI Content Engine',
    tagline: 'SEO-optimised content at scale — without the slop',
    description:
      'A fully automated content pipeline that produces high-quality, personality-rich blog posts, social media content, and copy that actually ranks.',
    icon: '✍️',
    features: [
      'SEO-optimised blog content with topical authority clusters',
      'Social media content calendar & generation',
      'Email newsletter automation',
      'Content repurposing (blog → LinkedIn → Twitter)',
      'Performance tracking & content gap analysis',
    ],
    idealFor: 'Brands that need consistent, ranking content without a full-time writer',
    priceSA: 'R 5,000 – R 20,000 /mo',
    priceIntl: '$500 – $2,000 /mo',
    cta: 'Start Your Content Engine',
  },
  {
    id: 'fullstack',
    title: 'Full AI Integration',
    tagline: 'End-to-end AI transformation for your entire business',
    description:
      'The complete package. Strategy, chatbots, automation, analytics, and content — all working together to transform how your business operates.',
    icon: '🚀',
    features: [
      'Everything in the packages above',
      'Custom AI solution architecture',
      'Team training & change management',
      '3-month support & optimisation',
      'Priority response & dedicated AI engineer',
    ],
    idealFor: 'Businesses ready for comprehensive AI transformation',
    priceSA: 'R 50,000 – R 150,000',
    priceIntl: '$5,000 – $15,000',
    cta: 'Transform Your Business',
  },
];

export default services;