# AI Agent HR

AI Agent HR adalah dashboard web dan backend demo untuk membantu tim HR dalam:
- screening kandidat otomatis
- chatbot HR berbasis policy
- monitoring KPI rekrutmen dan karyawan
- analisis performa onboarding

## Fitur utama
- Candidate screening berdasarkan job description dan CV
- Skor kecocokan kandidat (0-100)
- Chatbot HR untuk pertanyaan umum seperti cuti, benefit, dan payroll
- Dashboard KPI rekrutmen dan karyawan
- UI dashboard modern untuk demo produk

## Struktur proyek

```text
AIAgentResume/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── hr_agent.py
│   │   ├── kpi_service.py
│   │   └── sample_data.py
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── config.py
│   └── main.py
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
source .venv/bin/activate
```

2. Install dependency
```bash
pip install -r requirements.txt
```

3. Jalankan app
```bash
uvicorn app.main:app --reload
```

4. Buka browser
```text
http://localhost:8000/
```

## Endpoint utama
- GET /health
- GET /
- POST /api/screen-candidate
- POST /api/chat
- GET /api/kpi
- GET /api/dashboard

## Demo penggunaan
- Isi form screening kandidat di dashboard
- Klik Analyze Candidate
- Tanya ke HR assistant seperti:
  - Berapa cuti tahunan karyawan?
  - Apa benefit yang diberikan?
  - Bagaimana proses payroll?

## Catatan
Proyek ini adalah versi demo MVP, fokus pada alur HR digital dan dashboard interaktif. Untuk production, fitur berikut bisa ditambahkan:
- autentikasi HR admin
- database PostgreSQL / MySQL
- integrasi OpenAI atau LLM
- export report PDF/Excel
- onboarding workflow otomatis
