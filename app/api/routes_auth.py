from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/auth", tags=["auth"])


class AuthInput(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(auth_input: AuthInput):
    # Placeholder for authentication logic
    if auth_input.username == "admin" and auth_input.password == "password":
        token = create_token({"sub": auth_input.username})
        return {"access_token": token, "token_type": "bearer"}
    return {"error": "Invalid credentials"}