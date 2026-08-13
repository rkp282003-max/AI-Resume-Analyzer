import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def clean_json(text: str):
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)


def analyze_resume(resume_text: str):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze this resume.

Resume:
{resume_text}

Return ONLY valid JSON.

{{
    "ats_score": 0,
    "summary": "",
    "strengths": [],
    "missing_skills": [],
    "suggestions": [],
    "recommended_roles": [],
    "interview_questions": []
}}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return clean_json(response.text)


def compare_resume_with_job(resume_text: str, job_description: str):

    prompt = f"""
You are an ATS Resume Matching Expert.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY valid JSON.

{{
    "match_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "suggestions": []
}}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return clean_json(response.text)