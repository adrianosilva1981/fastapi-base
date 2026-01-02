from fastapi import HTTPException, status
from core.security import verify_password, create_access_token
from repository.user_repository import UserRepository


async def authenticate(username: str, password: str):
    user = await UserRepository.find_by_username_or_email(username)

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token(
        data={"sub": str(user["_id"])}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

