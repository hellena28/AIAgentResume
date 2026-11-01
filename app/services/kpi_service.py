from typing import Any, Dict


def build_dashboard_kpi() -> Dict[str, Any]:
    return {
        "hiring_cycle_days": 21,
        "candidate_match_score": 86,
        "cost_per_hire": 5200000,
        "employee_satisfaction": 4.4,
        "attrition_rate": 8.5,
        "training_completion": 91,
        "response_time_hr_bot_seconds": 90,
        "satisfaction_trend": "+6% vs bulan lalu",
        "recommendation": "Kinerja HR digital berada dalam tren positif. Fokuskan optimalisasi onboarding dan pemetaan KPI karyawan untuk menurunkan attrition.",
    }


def compute_kpi_metrics(values: Dict[str, Any]) -> Dict[str, Any]:
    metrics = values or {}
    return {
        "hiring_cycle_days": metrics.get("hiring_cycle_days", 21),
        "candidate_match_score": metrics.get("candidate_match_score", 86),
        "cost_per_hire": metrics.get("cost_per_hire", 5200000),
        "employee_satisfaction": metrics.get("employee_satisfaction", 4.4),
        "attrition_rate": metrics.get("attrition_rate", 8.5),
        "recommendation": (
            "Performansi HR efektif dan stabil. "
            "Tingkatkan kualitas pengalaman onboarding untuk menurunkan tingkat keluar karyawan."
        ),
    }
