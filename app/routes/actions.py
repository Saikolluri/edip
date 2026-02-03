from fastapi import APIRouter
from pydantic import BaseModel
from app.risk_engine import evaluate_risk

router = APIRouter()

class ActionInput(BaseModel):
    industry: str
    location: str
    action: str

class ActionAnalysisResponse(BaseModel):
    industry: str
    location: str
    action: str
    risk_level: str
    regulation: str
    clause: str
    explanation: str
    audit_note: str

@router.post("/analyze-action", response_model=ActionAnalysisResponse)
def analyze_action(data: ActionInput):
    risk_level, regulation, clause, explanation = evaluate_risk(
        data.industry,
        data.location,
        data.action
    )

    return {
        "industry": data.industry,
        "location": data.location,
        "action": data.action,
        "risk_level": risk_level,
        "regulation": regulation,
        "clause": clause,
        "explanation": explanation,
        "audit_note": "Decision derived from predefined compliance rules"
    }

