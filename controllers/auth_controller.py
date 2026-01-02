from fastapi import HTTPException, Request, status
from core.logger import setup_logger
from utils.http_utils import raise_unexpected_error
from domains.auth_domain import authenticate

logger = setup_logger(__name__)

async def auth(request: Request):
    try:
        auth_data = request.state.auth

        if not auth_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Missing authentication data"
            )
        
        return await authenticate(
            username=auth_data["username"],
            password=auth_data["password"]
        )

    except HTTPException:
        raise
    
    except Exception:
        logger.exception("Error in authentication controller")
        return raise_unexpected_error()
