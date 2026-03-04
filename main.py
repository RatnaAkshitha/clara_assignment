from fastapi import FastAPI
import json
import os

app = FastAPI()

@app.post("/process-demo")
async def process_demo():

    # Read transcript file
    with open("backend/transcript.txt", "r") as f:
        transcript = f.read()

    account_id = "bens-electric"

    os.makedirs("outputs", exist_ok=True)

    # Extract information from transcript
    crm = "Jobber" if "Jobber" in transcript else "Unknown"
    plan = "Starter Plan" if "Starter Plan" in transcript else "Unknown"
    minutes = 500 if "500 minutes" in transcript else None
    price = 249 if "$249" in transcript or "249" in transcript else None

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
        "message": "Files generated successfully",
        "files": [v1_path, v2_path]
    }






