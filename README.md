# AI Agent HR

AI Agent HR adalah solusi berbasis AI untuk membantu tim HR dalam rekrutmen, onboarding, dan monitoring kinerja karyawan.

## Fitur
- Screening CV otomatis berdasarkan job description
- Rekomendasi kandidat dengan skor kecocokan
- Chatbot HR untuk pertanyaan karyawan
- KPI dashboard untuk rekrutmen dan kinerja karyawan
- Template onboarding dan analisis performance

## Struktur proyek

```text
AIAgentResume/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── hr_agent.py
│   │   ├── kpi_service.py
│   │   └── sample_data.py
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   └── models.py
├── tests/
│   └── test_hr_agent.py
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Cara menjalankan

1. Buat virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

2. Install dependency
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi
```bash
uvicorn app.main:app --reload
```

4. Akses dokumentasi API
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoint utama
- `GET /health`
- `POST /screen-candidate`
- `POST /chat`
- `GET /kpi`
- `GET /dashboard`

## Contoh payload untuk screening kandidat
```json
{
  "job_title": "Senior Data Analyst",
  "job_description": "Mencari kandidat dengan pengalaman SQL, Python, dashboard, dan analisis data.",
  "candidate_name": "Rina Rahma",
  "resume_text": "Saya memiliki pengalaman 5 tahun di analisis data, SQL, Python, dashboard Power BI, dan stakeholder management."
}
```

## Roadmap
- Integrasi dengan OpenAI / LLM
- Integrasi database kandidat dan karyawan
- Modul onboarding otomatis
- Dashboard analytics lanjutan
- Notifikasi email dan Slack

## Lisensi
MIT
