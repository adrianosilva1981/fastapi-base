from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.excluded_paths = {"/"}

    async def dispatch(self, request: Request, call_next):
        try:
            if request.url.path in self.excluded_paths:
                return await call_next(request)

            token = request.headers.get("Authorization")
            # aqui tem que chamar a classe jwtservice para tentar validar o token
            if not token or token != "Bearer meu_token_secreto":
                raise HTTPException(status_code=401, detail="Não autorizado")

            return await call_next(request)

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

        except Exception as e:
            print(f"Erro inesperado: {str(e)}")  # 🔍 Debug no console
            return JSONResponse(status_code=500, content={"detail": "Unexpected error"})