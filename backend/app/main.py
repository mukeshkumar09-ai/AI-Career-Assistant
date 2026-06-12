from fastapi import FastAPI
from app.routes.resume import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Career Assistant Backend Running"}