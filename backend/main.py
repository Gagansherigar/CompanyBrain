from fastapi import FastAPI

from api.routes.health import router as health_router
from api.routes.chat import router as chat_router
from api.routes.ingest import router as ingest_router
from fastapi.middleware.cors import (
    CORSMiddleware
)

app = FastAPI(
    title="Organizational Intelligence System"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://company-brain-kappa.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health_router)
app.include_router(chat_router)
app.include_router(ingest_router)


@app.get("/")
def root():

    return {
        "message": "Organizational Intelligence System Running"
    }