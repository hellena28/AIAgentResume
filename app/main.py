from app.api.routes import router
from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Agent HR untuk rekrutmen, onboarding, dan KPI karyawan",
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok", "app": settings.APP_NAME, "version": settings.APP_VERSION}
