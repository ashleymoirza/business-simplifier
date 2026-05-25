/**
 * FAQ database for the AI chatbot
 * Covers all industry verticals + general AI consulting questions
 *
 * Each entry has: keywords (for matching), question, answer, category
 */

const faqs = [
  // ─── General AI Consulting ───
  {
    keywords: ['what is', 'ai consulting', 'do you do', 'services', 'offer'],
    question: 'What is AI consulting and what do you offer?',
    answer: 'We help businesses save ±R40K/year by streamlining processes with AI. We offer strategy sessions, custom chatbots, process automation, analytics dashboards, content engines, and full AI integration. Start with a free 1-hour consultation.',
    category: 'general',
  },
  {
    keywords: ['free', 'consultation', 'session', 'first step', 'get started'],
    question: 'How does the free consultation work?',
    answer: 'Book a 1-hour video call. We learn about your business, identify processes where AI can have the biggest impact, and give you a clear roadmap with estimated ROI. No commitment, no sales pitch.',
    category: 'general',
  },
  {
    keywords: ['cost', 'price', 'pricing', 'how much', 'fees', 'rates', 'expensive'],
    question: 'How much does AI consulting cost?',
    answer: 'It starts free with a 1-hour strategy session. Paid projects range from R7,500 (chatbots) to R150,000 (full integration). We have separate pricing for SA market (ZAR) and international clients (USD). See our /pricing page.',
    category: 'general',
  },
  {
    keywords: ['how long', 'timeline', 'delivery', 'timeframe', 'when'],
    question: 'How long does a typical project take?',
    answer: 'Most single-solution projects (chatbot, automation) take 5-10 days. Full integrations take 3-6 weeks. The free strategy session is 1 hour — you walk away with a roadmap.',
    category: 'general',
  },
  {
    keywords: ['technical', 'coding', 'code', 'developer', 'tech', 'need to know'],
    question: 'Do I need technical knowledge to work with you?',
    answer: 'Not at all. We handle all the technical work. You just need to understand your business processes and pain points. We translate those into AI solutions.',
    category: 'general',
  },
  {
    keywords: ['support', 'after', 'ongoing', 'maintenance', 'post launch'],
    question: 'Do you offer ongoing support after delivery?',
    answer: 'Yes. All paid plans include email support. Professional and Enterprise plans include priority support with a dedicated engineer and monthly strategy reviews.',
    category: 'general',
  },
  {
    keywords: ['satisfied', 'guarantee', 'revision', 'refund', 'not happy'],
    question: 'What if Im not satisfied with the work?',
    answer: 'We iterate until you\'re happy. Growth plans include 1 revision cycle. Professional and Enterprise include unlimited revisions. Your satisfaction is how we earn referrals.',
    category: 'general',
  },
  {
    keywords: ['roi', 'results', 'saving', 'save', 'money back', 'value'],
    question: 'What kind of ROI can I expect?',
    answer: 'Our clients typically save ±R40K/year by automating repetitive processes. Chatbots reduce support costs by 60%. Automation saves 20-40 hours/week in team time. We include ROI estimates in your free strategy session.',
    category: 'general',
  },
  {
    keywords: ['south africa', 'za', 'sa', 'location', 'based', 'where', 'africa'],
    question: 'Are you based in South Africa?',
    answer: 'Yes! We serve both the South African market (with affordable ZAR pricing) and international clients (USD pricing). Our consultations are remote via video call.',
    category: 'general',
  },
  {
    keywords: ['startup', 'sme', 'small business', 'medium business', 'size'],
    question: 'What size businesses do you work with?',
    answer: 'We specialise in SMEs and startups — from solo founders to companies with 200+ employees. If you have repetitive processes that could be automated, we can help.',
    category: 'general',
  },

  // ─── Chatbots ───
  {
    keywords: ['chatbot', 'chat bot', 'conversation', 'chat', 'messaging'],
    question: 'What kind of chatbots do you build?',
    answer: 'Custom AI chatbots trained on YOUR business data. They handle customer support, lead generation, FAQ answering, and internal knowledge base queries. Deployable on web, WhatsApp, and Slack.',
    category: 'chatbot',
  },
  {
    keywords: ['chatbot cost', 'chatbot price', 'how much chatbot'],
    question: 'How much does a custom chatbot cost?',
    answer: 'AI chatbots range from R7,500 to R25,000 (SA market) or $500 to $2,500 (international). Price depends on complexity, data sources, and number of channels.',
    category: 'chatbot',
  },
  {
    keywords: ['whatsapp', 'chatbot whatsapp', 'whatsapp bot'],
    question: 'Can you build a WhatsApp chatbot?',
    answer: 'Yes! We can deploy chatbots on WhatsApp, web chat, Slack, and Telegram. Multi-channel deployment is included in our chatbot packages.',
    category: 'chatbot',
  },

  // ─── Automation ───
  {
    keywords: ['automation', 'workflow', 'process', 'automate', 'repetitive'],
    question: 'What business processes can you automate?',
    answer: 'Email processing, document data extraction, invoice handling, CRM updates, approval chains, report generation, customer onboarding — if it\'s repetitive and rule-based, we can automate it.',
    category: 'automation',
  },
  {
    keywords: ['automation cost', 'automation price'],
    question: 'How much does process automation cost?',
    answer: 'Business process automation ranges from R15,000 to R50,000 (SA) or $1,500 to $5,000 (international). We include an automation audit in your free strategy session.',
    category: 'automation',
  },
  {
    keywords: ['document', 'invoice', 'email', 'data entry', 'paperwork'],
    question: 'Can AI handle document processing?',
    answer: 'Yes. AI extracts data from invoices, contracts, emails, and PDFs with 95%+ accuracy. It can populate your CRM, accounting software, or database automatically.',
    category: 'automation',
  },

  // ─── Analytics ───
  {
    keywords: ['analytics', 'dashboard', 'report', 'data analysis', 'insights', 'bi'],
    question: 'What kind of AI analytics do you provide?',
    answer: 'AI-powered dashboards that connect to your data sources, natural-language querying (ask questions in plain English), predictive analytics, and automated report generation.',
    category: 'analytics',
  },
  {
    keywords: ['predictive', 'forecast', 'trend', 'prediction'],
    question: 'Can AI predict my business trends?',
    answer: 'Yes. Our AI analytics include predictive modelling that forecasts sales trends, customer behaviour, inventory needs, and cash flow patterns based on your historical data.',
    category: 'analytics',
  },

  // ─── Content ───
  {
    keywords: ['content', 'blog', 'writing', 'seo', 'social media', 'marketing'],
    question: 'How does your AI content engine work?',
    answer: 'We set up an automated content pipeline that produces SEO-optimised blog posts, social media content, and email newsletters. Each piece includes personality, stats, and rich context — no generic AI slop.',
    category: 'content',
  },
  {
    keywords: ['content cost', 'content price'],
    question: 'How much does the AI content engine cost?',
    answer: 'The content engine subscription ranges from R5,000 to R20,000/month (SA) or $500 to $2,000/month (international), depending on volume and platforms.',
    category: 'content',
  },

  // ─── Healthcare ───
  {
    keywords: ['healthcare', 'medical', 'hospital', 'clinic', 'doctor', 'patient'],
    question: 'How can AI help healthcare businesses?',
    answer: 'AI in healthcare handles appointment scheduling, medical transcription, patient intake forms, insurance claim processing, and even assists with diagnostic image analysis. It reduces admin costs by up to 40%.',
    category: 'healthcare',
  },
  {
    keywords: ['healthcare ai', 'medical ai', 'health tech'],
    question: 'Is AI safe for medical use?',
    answer: 'We build AI that assists — not replaces — medical professionals. Our healthcare solutions focus on administrative automation (scheduling, billing, records) and decision support tools. All solutions comply with POPIA and relevant regulations.',
    category: 'healthcare',
  },

  // ─── Finance ───
  {
    keywords: ['finance', 'bank', 'insurance', 'fintech', 'accounting', 'financial'],
    question: 'How can AI help financial services?',
    answer: 'AI automates compliance checks (KYC/AML), fraud detection, regulatory reporting, and personalised customer recommendations. It processes thousands of transactions per second to flag anomalies.',
    category: 'finance',
  },
  {
    keywords: ['fraud detection', 'fraud', 'compliance', 'kyc', 'aml'],
    question: 'Can AI help with fraud detection and compliance?',
    answer: 'Absolutely. Machine learning models learn normal transaction patterns and flag anomalies in real time. AI also automates KYC/AML checks and regulatory report generation, saving hours of manual work.',
    category: 'finance',
  },

  // ─── E-commerce ───
  {
    keywords: ['ecommerce', 'e-commerce', 'online store', 'shop', 'retail', 'product'],
    question: 'How can AI improve my online store?',
    answer: 'AI powers product recommendations, personalised search, dynamic pricing, demand forecasting, and customer service chatbots. Our clients see 15-30% revenue increases from AI personalisation.',
    category: 'ecommerce',
  },
  {
    keywords: ['recommendation', 'personalisation', 'personalized'],
    question: 'How does AI product recommendations work?',
    answer: 'AI analyses customer browsing, purchase history, and similar customer behaviour to recommend the right products at the right time. This typically boosts average order value by 20-30%.',
    category: 'ecommerce',
  },
  {
    keywords: ['inventory', 'stock', 'demand forecast'],
    question: 'Can AI help with inventory management?',
    answer: 'Yes. AI predicts which products will be in demand, when, and at what price. This means fewer stockouts, less overstock, and better cash flow management.',
    category: 'ecommerce',
  },

  // ─── Education ───
  {
    keywords: ['education', 'school', 'university', 'training', 'learning', 'student'],
    question: 'How can AI help educational institutions?',
    answer: 'AI powers adaptive learning platforms that adjust to each student\'s pace, automated grading for assessments, and administrative automation for enrolment, scheduling, and reporting.',
    category: 'education',
  },
  {
    keywords: ['tutoring', 'tutor', 'personalised learning'],
    question: 'Can AI provide personalised tutoring?',
    answer: 'Yes. AI tutoring systems adapt difficulty, pace, and teaching style to each student. Students who master concepts quickly move ahead, while those who struggle get additional practice.',
    category: 'education',
  },
  {
    keywords: ['grading', 'assessment', 'marking'],
    question: 'Can AI automate grading?',
    answer: 'AI handles multiple-choice and short-answer grading instantly, and can score essays against consistent rubrics. This saves teachers up to 40% of their grading time.',
    category: 'education',
  },

  // ─── Real Estate ───
  {
    keywords: ['real estate', 'property', 'agent', 'realtor', 'estate'],
    question: 'How can AI help real estate agents?',
    answer: 'AI automates lead qualification, generates virtual property tours, provides predictive pricing, and handles buyer enquiries 24/7. Agents using AI close more deals with less effort.',
    category: 'realestate',
  },
  {
    keywords: ['lead gen', 'lead generation', 'buyer', 'seller'],
    question: 'Can AI generate real estate leads?',
    answer: 'AI analyses visitor behaviour on your property listings to identify hot leads, then automatically follows up with personalised property recommendations — converting more browsers into buyers.',
    category: 'realestate',
  },
  {
    keywords: ['valuation', 'pricing', 'home value', 'property value'],
    question: 'Can AI predict property values?',
    answer: 'Yes. AI models analyse comparable sales, market trends, and property features to suggest optimal listing prices and predict final sale prices with impressive accuracy.',
    category: 'realestate',
  },

  // ─── Legal ───
  {
    keywords: ['legal', 'lawyer', 'law firm', 'attorney', 'contract', 'compliance'],
    question: 'How can AI help legal practices?',
    answer: 'AI reviews contracts in minutes, flags risky clauses, ensures regulatory compliance, and accelerates due diligence. Lawyers using AI cut document review time by up to 80%.',
    category: 'legal',
  },
  {
    keywords: ['contract review', 'document review', 'due diligence'],
    question: 'Can AI review contracts?',
    answer: 'Yes. AI reads contracts and extracts key terms, obligations, and risks. It flags unfavourable clauses, compares against standard templates, and identifies missing provisions — in minutes instead of hours.',
    category: 'legal',
  },

  // ─── Manufacturing ───
  {
    keywords: ['manufacturing', 'factory', 'production', 'plant', 'quality control'],
    question: 'How can AI help manufacturing businesses?',
    answer: 'AI powers visual quality control (catching defects human eyes miss), predictive maintenance (reducing downtime by 50%), and production schedule optimisation.',
    category: 'manufacturing',
  },
  {
    keywords: ['predictive maintenance', 'maintenance', 'downtime'],
    question: 'What is predictive maintenance?',
    answer: 'AI analyses vibration, temperature, and acoustic data from machinery to predict failures before they happen. This reduces unplanned downtime by up to 50% and extends equipment life.',
    category: 'manufacturing',
  },
  {
    keywords: ['quality', 'defect', 'inspection', 'vision'],
    question: 'Can AI do visual quality inspection?',
    answer: 'Yes. Computer vision systems inspect products at line speed, catching micro-cracks, colour variations, packaging defects, and assembly errors invisible to the human eye.',
    category: 'manufacturing',
  },

  // ─── Logistics ───
  {
    keywords: ['logistics', 'supply chain', 'delivery', 'fleet', 'warehouse', 'transport'],
    question: 'How can AI help logistics companies?',
    answer: 'AI optimises delivery routes in real time, predicts fleet maintenance needs, and optimises warehouse bin placement and picking routes. Savings of 15-30% on fuel and 40% faster picking.',
    category: 'logistics',
  },
  {
    keywords: ['route optimisation', 'route', 'fuel', 'delivery route'],
    question: 'Can AI optimise my delivery routes?',
    answer: 'Yes. AI plans routes that adapt to traffic, weather, and order changes in real time. This reduces fuel costs by 15-30% and increases deliveries per shift by 20%.',
    category: 'logistics',
  },
  {
    keywords: ['fleet', 'fleet management', 'vehicle', 'truck'],
    question: 'Can AI help manage my fleet?',
    answer: 'AI predicts maintenance needs before breakdowns happen, monitors driver behaviour for safety, and optimises vehicle utilisation across your entire fleet.',
    category: 'logistics',
  },

  // ─── Implementation ───
  {
    keywords: ['how it works', 'process', 'method', 'approach', 'pipeline'],
    question: 'What is your delivery process?',
    answer: 'Discovery (free 1hr) → Audit (deep analysis) → Build (rapid AI development) → Deploy (launch + training) → Support (ongoing optimisation). Most single-solution projects take 5-10 days.',
    category: 'implementation',
  },
  {
    keywords: ['data', 'data security', 'privacy', 'popia', 'gdpr', 'safe'],
    question: 'What about data security and privacy?',
    answer: 'We take data security seriously. All client data is handled according to POPIA (SA) and GDPR (EU) standards. We sign NDAs and can work with your existing security protocols.',
    category: 'implementation',
  },
  {
    keywords: ['contract', 'commitment', 'lock-in', 'long term'],
    question: 'Is there a long-term contract?',
    answer: 'No lock-in contracts. The free consultation has no commitment. Paid projects are scoped per project. Ongoing support is month-to-month.',
    category: 'implementation',
  },
  {
    keywords: ['compete', 'competitor', 'competition', 'unique', 'different'],
    question: 'What makes you different from other AI consultants?',
    answer: 'We\'re AI-native — we use the best AI tools available to deliver faster, at better quality, and at a fraction of traditional costs. Plus, we start with a free session so there\'s zero risk.',
    category: 'implementation',
  },
];

/**
 * Find the best matching FAQ for a user query
 * Uses keyword matching with scoring
 * @param {string} query
 * @returns {{ faq: object|null, score: number }}
 */
export function findBestMatch(query) {
  if (!query || query.trim().length < 2) return { faq: null, score: 0 };

  const words = query.toLowerCase().split(/\s+/).filter(w => w.length > 2);

  let bestScore = 0;
  let bestFaq = null;

  for (const faq of faqs) {
    let score = 0;
    for (const word of words) {
      for (const keyword of faq.keywords) {
        if (keyword.includes(word)) {
          score += 3;
        }
        if (word.includes(keyword) || keyword.includes(word)) {
          score += 2;
        }
        if (faq.question.toLowerCase().includes(word)) {
          score += 1;
        }
        if (faq.answer.toLowerCase().includes(word)) {
          score += 0.5;
        }
      }
    }
    if (score > bestScore) {
      bestScore = score;
      bestFaq = faq;
    }
  }

  return { faq: bestFaq, score: bestScore };
}

/**
 * Get all FAQs grouped by category
 */
export function getFaqsByCategory() {
  const grouped = {};
  for (const faq of faqs) {
    if (!grouped[faq.category]) grouped[faq.category] = [];
    grouped[faq.category].push(faq);
  }
  return grouped;
}

export default faqs;