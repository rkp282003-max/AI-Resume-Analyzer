from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.resume import Resume
from app.database import Base, engine
from app.models.user import User
from app.api.user import router as user_router
from app.api.resume import router as resume_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Resume Analyzer API")

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------------------------------

app.include_router(user_router)
app.include_router(resume_router)


@app.get("/")
def home():
    return {"message": "Welcome to AI Resume Analyzer API"}


@app.get("/health")
def health():
    return {"status": "Running"}