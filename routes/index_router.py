from fastapi import APIRouter
from dotenv import load_dotenv
import os

index_router  = APIRouter()

load_dotenv()

@index_router.get('/')
async def healthcheck():
    return {
        "name": os.getenv('APP_NAME'),
        "version": os.getenv('APP_VERSION')
    }