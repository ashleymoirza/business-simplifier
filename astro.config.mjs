// @ts-check
import { defineConfig } from 'astro/config';
import alpinejs from '@astrojs/alpinejs';

// https://astro.build/config
export default defineConfig({
  site: 'https://businesssimplifier.co.za',
  integrations: [alpinejs()],
  vite: {
    server: {
      proxy: {
        // During dev: proxy /api/* to the FastAPI backend on port 8001
        // Start backend first: cd "AI Consultation" && bash backend/start.sh
        '/api': {
          target: 'http://localhost:8001',
          changeOrigin: true,
        },
      },
    },
  },
});