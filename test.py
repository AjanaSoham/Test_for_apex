import os
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/test-lm-studio")
def test_lm_studio():
    base_url = os.getenv("LM_STUDIO_BASE_URL")

    if not base_url:
        return {
            "ok": False,
            "error": "LM_STUDIO_BASE_URL is missing"
        }

    try:
        response = requests.get(
            f"{base_url.rstrip('/')}/models",
            timeout=20
        )

        return {
            "ok": response.ok,
            "status_code": response.status_code,
            "response": response.json()
        }

    except Exception as error:
        return {
            "ok": False,
            "error_type": type(error).__name__,
            "error": str(error)
        }