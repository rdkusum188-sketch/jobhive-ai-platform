from __future__ import annotations

from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_jobs(candidate_profile: str, job_records: List[str]) -> List[float]:
    if not job_records:
        return []

    texts = [candidate_profile] + job_records
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(texts)
    similarity = cosine_similarity(vectors[0:1], vectors[1:])
    return similarity[0].tolist()
