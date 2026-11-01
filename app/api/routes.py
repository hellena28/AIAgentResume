from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models import (
    HRChatRequest,
    HRChatResponse,
    KPIRequest,
    KPIResponse,
    ScreeningRequest,
    ScreeningResult,
)
from app.services.hr_agent import answer_hr_question, screen_candidate
from app.services.kpi_service import build_dashboard_kpi, compute_kpi_metrics
from app.services.sample_data import get_hr_policy_documents, get_sample_candidates

router = APIRouter(prefix="/api")


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/screen-candidate", response_model=ScreeningResult)
def screen_candidate_endpoint(request: ScreeningRequest):
    return screen_candidate(request)


@router.post("/chat", response_model=HRChatResponse)
def chat_endpoint(request: HRChatRequest):
    policy_docs = get_hr_policy_documents()
    answer = answer_hr_question(request.question, policy_docs)
    return HRChatResponse(answer=answer, source="hr_policy_knowledge_base")


@router.get("/kpi")
def get_kpi():
    return build_dashboard_kpi()


@router.post("/kpi")
def post_kpi(payload: KPIRequest):
    data = compute_kpi_metrics(payload.model_dump(exclude_none=True))
    return KPIResponse(**data)


@router.get("/dashboard")
def dashboard():
    sample = get_sample_candidates()
    summary = {
        "job_title": sample["job_title"],
        "job_description": sample["job_description"],
        "candidate_count": len(sample["candidates"]),
        "kpis": build_dashboard_kpi(),
    }
    return summary


@router.get("/demo-candidates")
def demo_candidates():
    return get_sample_candidates()
