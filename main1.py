from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

class RequestData(BaseModel):
    account_id: str

@app.post("/process-demo")
async def process_demo(req: RequestData):

    account_id = req.account_id

    # read transcript from file
    with open("backend/transcript.txt", "r") as f:
        transcript = f.read().lower()

    os.makedirs("outputs", exist_ok=True)

    # -------- Extract simple info from transcript --------
    crm = "Jobber" if "jobber" in transcript else "Unknown"
    plan = "Starter Plan" if "starter plan" in transcript else "Unknown"
    minutes = 500 if "500" in transcript and "minute" in transcript else None
    price = 249 if "249" in transcript else None

    # -------- V1 Agent --------
    v1_agent = {
        "account_name": account_id,
        "version": "v1",
        "crm": crm,
        "services": [
            "Outlet replacement",
            "EV charger installation",
            "Hot tub wiring",
            "Electrical troubleshooting"
        ]
    }

    # -------- V2 Agent --------
    v2_agent = {
        "account_name": account_id,
        "version": "v2",
        "plan": plan,
        "minutes_per_month": minutes,
        "price_per_month": price
    }

    v1_path = f"outputs/{account_id}_v1.json"
    v2_path = f"outputs/{account_id}_v2.json"

    with open(v1_path, "w") as f:
        json.dump(v1_agent, f, indent=2)

    with open(v2_path, "w") as f:
        json.dump(v2_agent, f, indent=2)

    return {
        "message": "Agents generated",
        "v1_agent": v1_agent,
        "v2_agent": v2_agent
    }