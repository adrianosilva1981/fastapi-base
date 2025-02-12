from fastapi import FastAPI
from routes import index_router
from routes import user_router
from middlewares.AuthMiddleware import AuthMiddleware

app = FastAPI()

app.add_middleware(AuthMiddleware)

app.include_router(index_router, prefix="", tags=["Index"])
app.include_router(user_router, prefix="/users", tags=["Users"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)