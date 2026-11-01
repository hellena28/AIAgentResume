from typing import List, Optional

from pydantic import BaseModel, Field


class ScreeningRequest(BaseModel):
    job_title: str = Field(..., description="Nama posisi yang dilamar")
    job_description: str = Field(..., description="Deskripsi pekerjaan")
    candidate_name: str = Field(..., description="Nama kandidat")
    resume_text: str = Field(..., description="Isi resume kandidat")
    skills: Optional[List[str]] = Field(default=None, description="Skill tambahan yang ingin dibandingkan")


class ScreeningResult(BaseModel):
    candidate_name: str
    job_title: str
    match_score: int
    recommendation: str
    summary: str
    strengths: List[str]
    gaps: List[str]


class HRChatRequest(BaseModel):
    question: str = Field(..., description="Pertanyaan yang diajukan ke HR AI")


class HRChatResponse(BaseModel):
    answer: str
    source: str


class KPIRequest(BaseModel):
    hiring_cycle_days: Optional[int] = None
    candidate_match_score: Optional[float] = None
    cost_per_hire: Optional[float] = None
    employee_satisfaction: Optional[float] = None
    attrition_rate: Optional[float] = None


class KPIResponse(BaseModel):
    hiring_cycle_days: float
    candidate_match_score: float
    cost_per_hire: float
    employee_satisfaction: float
    attrition_rate: float
    recommendation: str
