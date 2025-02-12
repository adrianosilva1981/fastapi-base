from fastapi import APIRouter, HTTPException
from repositories import userRepository
from starlette import status

router = APIRouter()

@router.get('/')
async def getUsers():
    try:
        return await userRepository.getUsers()
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error_message)
