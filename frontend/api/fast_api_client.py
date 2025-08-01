import httpx

FASTAPI_URL = "http://localhost:8000/api/chat"
HEADERS = {
    "Authorization": "Bearer my-secret-token",  # Must match the token in auth.py
}

async def fetch_bot_response(message: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            FASTAPI_URL,
            json={"message": message},
            headers=HEADERS,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["response"]