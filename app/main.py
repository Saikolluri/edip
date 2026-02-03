from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .models import Base
from .routes.actions import router as action_router

app = FastAPI(title="EDIP - Explainable Decision Impact Platform")

# -------- CORS CONFIG --------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(action_router)

@app.get("/")
def root():
    return {"message": "EDIP backend running successfully"}

