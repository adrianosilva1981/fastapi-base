from fastapi import APIRouter, Request
from controllers.user_controller import create_user

user_router = APIRouter()

@user_router.post('/create')
async def create(request: Request): return await create_user(request)