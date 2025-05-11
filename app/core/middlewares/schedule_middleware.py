import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import structlog

from app.core.logger import logger
from app.utils.remove_sensetive_headers import remove_headers


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        trace_id = request.headers.get("X-TRACE-ID", str(uuid.uuid4()))
        structlog.contextvars.bind_contextvars(trace_id=trace_id)

        logger.info(
            "Request",
            method=request.method,
            header=remove_headers(dict(request.headers)),
            url=request.url.path,
            query_params=dict(request.query_params),
            client_host=request.client.host,
            trace_id=trace_id,
            user_agent=request.headers.get("user-agent"),
        )

        response = await call_next(request)
        structlog.contextvars.bind_contextvars(status_code=response.status_code)

        logger.info(
            "Response",
            status_code=response.status_code,
            duration=f"{(time.time() - start_time):.4f}s",
        )

        response.headers["x-trace-id"] = trace_id

        return response
