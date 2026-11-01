from app.services.hr_agent import answer_hr_question, screen_candidate


def test_screen_candidate_returns_valid_score():
    request = {
        "job_title": "Senior Data Analyst",
        "job_description": "Mencari kandidat dengan SQL, Python, Power BI, dashboard, dan analisis data.",
        "candidate_name": "Rina Rahma",
        "resume_text": "Saya berpengalaman 5 tahun dalam analisis data, SQL, Python, dashboard, dan Power BI.",
    }

    result = screen_candidate(type("Req", (), request)())

    assert 0 <= result.match_score <= 100
    assert result.candidate_name == "Rina Rahma"
    assert "summary" in result.model_dump()


def test_answer_hr_question_for_leave():
    answer = answer_hr_question("Berapa cuti tahunan karyawan?", [
        "Karyawan berhak mendapatkan cuti tahunan sesuai masa kerja dan kebijakan perusahaan.",
        "Benefit karyawan mencakup asuransi kesehatan dan tunjangan keluarga."
    ])

    assert "cuti" in answer.lower()
