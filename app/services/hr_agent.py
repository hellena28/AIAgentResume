import re
from typing import List, Set

from app.models import ScreeningRequest, ScreeningResult


COMMON_HR_KEYWORDS = {
    "recruitment",
    "hiring",
    "candidate",
    "interview",
    "screening",
    "onboarding",
    "performance",
    "kpi",
    "employee",
    "salary",
    "benefit",
    "cuti",
    "leave",
    "policy",
    "team",
    "stakeholder",
    "communication",
    "analysis",
    "analyst",
    "data",
    "sql",
    "python",
    "powerbi",
    "dashboard",
    "product",
    "manager",
    "project",
    "strategy",
    "hr",
    "people",
    "management",
}


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9\s]", " ", text.lower())


def _extract_keywords(text: str) -> Set[str]:
    cleaned = _normalize(text)
    words = set(cleaned.split())
    return words | (COMMON_HR_KEYWORDS & words)


def _extract_years_experience(text: str) -> int:
    match = re.search(r"(\d+)\s*\+?\s*(?:tahun|year|years)", _normalize(text))
    if match:
        return int(match.group(1))
    return 0


def screen_candidate(request: ScreeningRequest) -> ScreeningResult:
    job_text = f"{request.job_title} {request.job_description}"
    job_keywords = _extract_keywords(job_text)
    resume_keywords = _extract_keywords(request.resume_text)

    overlap = sorted(job_keywords & resume_keywords)
    coverage = len(overlap)
    total_keywords = max(len(job_keywords), 1)
    similarity_score = min(100, round((coverage / total_keywords) * 100))

    experience_score = min(25, max(0, _extract_years_experience(request.resume_text) * 5))
    custom_skill_bonus = 0
    if getattr(request, "skills", None):
        requested = {skill.lower() for skill in request.skills}
        found = requested & resume_keywords
        custom_skill_bonus = min(20, len(found) * 10)

    total_score = min(100, similarity_score + experience_score + custom_skill_bonus)

    strengths = sorted({word for word in overlap if word.isalpha() and len(word) > 3})[:5]
    if not strengths:
        strengths = ["Komunikasi", "Adaptabilitas", "Analitis"]

    gaps = []
    missing = sorted(job_keywords - resume_keywords)
    for item in missing[:5]:
        if item and len(item) > 2:
            gaps.append(item)

    recommendation = (
        "Sangat cocok" if total_score >= 80 else "Cocok dengan review tambahan" if total_score >= 60 else "Perlu evaluasi lanjutan"
    )
    summary = (
        f"{request.candidate_name} memiliki kecocokan {total_score}% untuk posisi {request.job_title}. "
        f"Kandidat menunjukkan overlap utama pada {', '.join(overlap[:5]) if overlap else 'kompetensi inti'} "
        f"dan pengalaman yang relevan dengan kebutuhan role."
    )

    return ScreeningResult(
        candidate_name=request.candidate_name,
        job_title=request.job_title,
        match_score=total_score,
        recommendation=recommendation,
        summary=summary,
        strengths=strengths,
        gaps=gaps,
    )


def answer_hr_question(question: str, policy_docs: List[str]) -> str:
    normalized_question = _normalize(question)
    question_words = set(normalized_question.split())

    if not policy_docs:
        return "Saya belum memiliki basis policy yang cukup. Silakan tambahkan dokumen HR atau SOP terkait."

    best_match = None
    best_score = 0

    for doc in policy_docs:
        doc_words = set(_normalize(doc).split())
        score = len(question_words & doc_words)
        if score > best_score:
            best_score = score
            best_match = doc

    if best_match and best_score > 0:
        return best_match

    if "cuti" in normalized_question or "leave" in normalized_question:
        return "Karyawan berhak mendapatkan cuti sesuai ketentuan yang berlaku. Durasi cuti tahunan dan prosedur pengajuan disesuaikan dengan kebijakan perusahaan serta masa kerja."

    if "benefit" in normalized_question or "tunjangan" in normalized_question:
        return "Benefit karyawan mencakup kesehatan, tunjangan keluarga, dan fasilitas kerja sesuai peraturan internal perusahaan. Detail dapat dilihat di HRIS atau handbook karyawan."

    if "payroll" in normalized_question or "gaji" in normalized_question:
        return "Proses payroll dilakukan sesuai jadwal perusahaan dan dipotong berdasarkan aturan internal yang berlaku. Karyawan dapat mengajukan klarifikasi kepada tim HR."

    return "Saya belum menemukan jawaban yang relevan. Mohon sampaikan pertanyaan yang lebih spesifik mengenai kebijakan HR, payroll, benefit, atau cuti."
