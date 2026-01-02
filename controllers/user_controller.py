from fastapi import HTTPException, Request, status
from core.logger import setup_logger
from utils.http_utils import raise_unexpected_error
from domains.user_domain import register

logger = setup_logger(__name__)

async def create_user(request: Request):
    try:
        user_data = request.state.user_payload
        return await register(user_data)
    except HTTPException:
        raise
    
    except Exception:
        logger.exception("Error in user creation controller")
        return raise_unexpected_error()
