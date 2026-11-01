from app.models import ScreeningRequest

SAMPLE_JOB_DESCRIPTION = """
Senior Data Analyst
Mencari kandidat dengan pengalaman analisis data, SQL, Python, dashboard, stakeholder management, dan komunikasi bisnis.
Kualifikasi:
- 3+ tahun pengalaman di analisis data
- Mahir SQL, Python, Excel, Power BI
- Mampu membuat dashboard dan insight bisnis
- Berkomunikasi efektif dengan stakeholder
"""

SAMPLE_RESUMES = {
    "Rina Rahma": """
    Saya adalah Data Analyst dengan 5 tahun pengalaman.
    Menguasai SQL, Python, Power BI, dashboard, dan analisis KPI.
    Terbiasa bekerja dengan stakeholder dan menyusun insight bisnis.
    """,
    "Dimas Putra": """
    Saya memiliki pengalaman di proyek digital marketing.
    Fokus pada strategi dan analisis pasar, komunikasi, dan manajemen proyek.
    """,
}


def get_sample_candidates() -> dict:
    return {
        "job_title": "Senior Data Analyst",
        "job_description": SAMPLE_JOB_DESCRIPTION,
        "candidates": [
            {
                "candidate_name": "Rina Rahma",
                "resume_text": SAMPLE_RESUMES["Rina Rahma"],
            },
            {
                "candidate_name": "Dimas Putra",
                "resume_text": SAMPLE_RESUMES["Dimas Putra"],
            },
        ],
    }


def get_hr_policy_documents() -> list[str]:
    return [
        "Karyawan berhak mendapatkan cuti tahunan sesuai masa kerja dan kebijakan perusahaan. Pengajuan cuti harus dilakukan minimal 3 hari kerja sebelum tanggal cuti.",
        "Benefit karyawan mencakup asuransi kesehatan, tunjangan keluarga, dan fasilitas kerja sesuai peraturan internal perusahaan.",
        "Payroll dibayarkan setiap tanggal 25 setiap bulannya dan dapat dikonfirmasi melalui HRIS atau tim payroll.",
    ]
