import os
import shutil
import json

from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session
from app.schemas.job import JobDescription
from app.utils.pdf_parser import extract_text_from_pdf
from app.services.ai_analyzer import compare_resume_with_job
from app.database import get_db
from app.models.resume import Resume
from app.utils.pdf_parser import extract_text_from_pdf
from app.services.ai_analyzer import analyze_resume

router = APIRouter(prefix="/resume", tags=["Resume"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(file_path)

    # Analyze resume using AI
    analysis = analyze_resume(extracted_text)

    # Save to database
    new_resume = Resume(
        filename=file.filename,
        resume_text=extracted_text,
        analysis=json.dumps(analysis)
    )

    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    # Return response
    return {
        "message": "Resume analyzed successfully",
        "resume_id": new_resume.id,
        "filename": file.filename,
        "analysis": analysis
    }


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    resumes = db.query(Resume).all()

    history = []

    for resume in resumes:
        history.append({
            "id": resume.id,
            "filename": resume.filename,
            "analysis": json.loads(resume.analysis)
        })

    return history

@router.post("/match")
async def match_resume(
    file: UploadFile = File(...),
    job: str = File(...)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    analysis = compare_resume_with_job(
        resume_text,
        job
    )

    return analysis