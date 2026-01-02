from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AuthContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        request.state.auth = None

        if request.url.path.startswith("/auth") and request.method == "POST":

            content_type = request.headers.get("content-type", "")

            if "application/json" in content_type:
                body = await request.json()
            else:
                form = await request.form()
                body = dict(form)

            username = body.get("username")
            password = body.get("password")

            if not username or not password:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={"detail": "Username and password are required"}
                )

            request.state.auth = {
                "username": username,
                "password": password
            }

        return await call_next(request)
