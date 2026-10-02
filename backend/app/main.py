from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="JobHive AI Platform")


class JobPayload(BaseModel):
    title: str
    company: str
    location: str = "Remote"
    salary: str = "Not disclosed"
    skills: str
    description: str


class CandidatePayload(BaseModel):
    name: str
    skills: str
    experience: str = ""
    bio: str = ""


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/jobs")
def get_jobs():
    data_file = Path(__file__).resolve().parent / "data" / "jobs.json"
    if not data_file.exists():
        return []
    return json.loads(data_file.read_text(encoding="utf-8"))


@app.get("/candidates")
def get_candidates():
    data_file = Path(__file__).resolve().parent / "data" / "candidates.json"
    if not data_file.exists():
        return []
    return json.loads(data_file.read_text(encoding="utf-8"))


@app.post("/jobs")
def create_job(payload: JobPayload):
    return {"message": "Job created", "job": payload.model_dump()}


@app.post("/candidates")
def create_candidate(payload: CandidatePayload):
    return {"message": "Candidate created", "candidate": payload.model_dump()}


@app.get("/seed")
def seed_data():
    return {"message": "Seed data loaded"}
