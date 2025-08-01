from fastapi import Header, HTTPException

async def verify_user(authorization: str = Header(...)):
    if authorization != "Bearer my-secret-token":
        raise HTTPException(status_code=403, detail="Unauthorized")
