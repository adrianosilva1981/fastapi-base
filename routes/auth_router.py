from fastapi import APIRouter, Request
from controllers.auth_controller import auth

auth_router = APIRouter()

@auth_router.post('/')
async def authtentication(request: Request): return await auth(request)