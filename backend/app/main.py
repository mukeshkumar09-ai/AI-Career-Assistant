from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.resume import router
from app.routes.jd import router as jd_router
from app.routes.match import router as match_router
from app.routes.analyze import router as analyze_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(jd_router)
app.include_router(match_router)
app.include_router(analyze_router)

@app.get("/")
def home():
    return {
        "message": "AI Career Assistant Backend Running"
    }