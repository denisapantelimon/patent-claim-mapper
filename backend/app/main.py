from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.patents import router as patent_router

app = FastAPI(
    title="Patent Infringement Search Tool"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patent_router)

@app.get("/")
async def root():
    return {
        "message": "Patent analyzer running"
    }