import time

import structlog
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.logger = structlog.get_logger()

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        self.logger.info(
            "Request received", method=request.method, path=request.url.path
        )

        response = await call_next(request)

        duration = time.time() - start_time
        self.logger.info(
            "Request processed",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration=duration,
        )

        return response
