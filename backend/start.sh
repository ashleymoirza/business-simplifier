#!/bin/bash
# Start the BusinessSimplifier audit backend
# Run from the "AI Consultation" directory:
#   cd "AI Consultation" && bash backend/start.sh

set -e

# Load .env if it exists
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

echo "Starting BusinessSimplifier Audit API on port 8001..."
echo "LLM provider: ${LLM_PROVIDER:-fcc}"
echo ""
echo "The Astro dev server (npm run dev) proxies /api/* to this server."
echo "Keep this terminal open alongside your Astro dev server."
echo ""

uv run uvicorn backend.main:app --port 8001 --reload --log-level info
