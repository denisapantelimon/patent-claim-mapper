# Patent Infringement Search Tool

AI-powered patent analysis system that identifies potentially infringing products and generates evidence-grounded claim charts.

## Features

- Patent claim parsing using LLMs
- Product discovery via web search
- Evidence extraction from public sources
- Claim-to-product mapping
- Structured claim chart generation
- FastAPI backend + Svelte frontend

## Tech Stack

### Frontend
- Svelte 5
- TypeScript
- Vite

### Backend
- Python
- FastAPI
- OpenAI API
- Trafilatura
- DuckDuckGo Search

---

# Project Structure

```bash
backend/
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── data/

frontend/
├── src/
├── public/
└── package.json