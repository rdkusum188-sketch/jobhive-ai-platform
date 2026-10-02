# JobHive AI Platform

A professional AI-powered job opportunity platform that helps candidates discover the best-fit roles using intelligent matching based on skills, experience, and job requirements.

## Features

- AI-powered job matching engine
- job listings and candidate profiles
- modern responsive frontend
- FastAPI backend with SQLite persistence
- seed data for quick demo setup
- production-ready project structure

## Tech Stack

- Frontend: React + Vite
- Backend: FastAPI + SQLAlchemy
- Database: SQLite
- AI Matching: scikit-learn TF-IDF + cosine similarity

## Quick Start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm install axios
npm run dev
```

Open:
- Frontend: http://localhost:5173
- Backend: http://localhost:8000

## API Endpoints

- GET /health
- GET /jobs
- POST /jobs
- GET /candidates
- POST /candidates
- GET /match/{candidate_id}
- GET /seed

## Demo

The app loads sample jobs and candidate profiles automatically via `/seed` and ranks the best job matches using AI similarity scoring.

## Project Structure

```text
jobhive-ai-platform/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   └── services/
│   │       └── matcher.py
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

## License

This project is intended for educational and demo use.
