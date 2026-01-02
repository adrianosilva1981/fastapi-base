from datetime import datetime, timezone
from fastapi import HTTPException, status
from core.security import get_password_hash, verify_password, create_access_token
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


async def register(user_data: dict):
    existing_user = await UserRepository.find_by_username_or_email(
        user_data["username"]
    )
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists"
        )
        
    user_data["password"] = get_password_hash(user_data["password"])
    user_data["created_at"] = datetime.now(timezone.utc)
    
    new_user = await UserRepository.create_user(user_data)
    
    return new_user