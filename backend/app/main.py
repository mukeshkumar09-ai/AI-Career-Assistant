from app.routes.match import router as match_router
from app.routes.jd import router as jd_router
from fastapi import FastAPI
from app.routes.resume import router

app = FastAPI()

app.include_router(router)
app.include_router(jd_router)
app.include_router(match_router)

@app.get("/")
def home():
    return {"message": "AI Career Assistant Backend Running"}