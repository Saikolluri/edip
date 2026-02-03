def evaluate_risk(industry: str, location: str, action: str):
    industry = industry.lower()
    action = action.lower()
    location = location.lower()

    risk_level = "Low"
    regulation = "None"
    clause = "N/A"
    explanation = "No significant regulatory risk detected."

    # ---- Personal data rules (India) ----
    if "data" in action and location == "india":

        regulation = "Information Technology Act, 2000"
        clause = "Section 43A"

        if industry in ["healthcare", "medical", "hospital"]:
            risk_level = "High"
            explanation = (
                "Sensitive personal data in healthcare requires stricter protection "
                "and increases compliance risk."
            )

        elif industry in ["it", "legal services", "legal"]:
            risk_level = "Medium"
            explanation = (
                "Personal data collection triggers data protection obligations "
                "under reasonable security practices."
            )

        else:
            risk_level = "Low"
            explanation = (
                "Limited personal data usage with lower regulatory exposure."
            )

    # ---- Financial data ----
    if "financial" in action:
        risk_level = "High"
        regulation = "Financial Regulations & RBI Guidelines"
        clause = "Data Security & KYC Norms"
        explanation = (
            "Handling financial data involves strict regulatory oversight "
            "and high compliance risk."
        )

    return risk_level, regulation, clause, explanation

