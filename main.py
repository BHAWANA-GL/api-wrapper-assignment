from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# External APIs ke URL
VAPI_URL = "https://api.vapi.ai/assistant/create"
RETELL_URL = "https://api.retellai.com/assistant/create"


@app.post("/create-agent/")
async def create_agent(agent_name: str, agent_description: str, api_choice: str):
    if api_choice not in ["vapi", "retell"]:
        raise HTTPException(
            status_code=400, detail="Invalid API choice. Choose either 'vapi' or 'retell'.")

    payload = {
        "agent_name": agent_name,
        "agent_description": agent_description
    }

    if api_choice == "vapi":
        response = requests.post(VAPI_URL, json=payload)
    elif api_choice == "retell":
        response = requests.post(RETELL_URL, json=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail="Error calling external API.")

    return response.json()
