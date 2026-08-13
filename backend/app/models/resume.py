from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    resume_text = Column(Text)
    analysis = Column(Text)