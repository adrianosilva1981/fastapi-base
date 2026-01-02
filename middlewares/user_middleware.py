from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class UserContextMiddleware(BaseHTTPMiddleware):

    REQUIRED_FIELDS = {"username", "email", "password"}

    async def dispatch(self, request: Request, call_next):

        request.state.user_payload = None

        if request.url.path == "/users/create" and request.method == "POST":

            content_type = request.headers.get("content-type", "")

            if "application/json" in content_type:
                body = await request.json()
            else:
                form = await request.form()
                body = dict(form)

            missing = self.REQUIRED_FIELDS - body.keys()
            if missing:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        "detail": f"Missing required fields: {', '.join(missing)}"
                    }
                )

            request.state.user_payload = body

        return await call_next(request)
