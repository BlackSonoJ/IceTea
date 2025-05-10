import asyncio

import uvicorn

from app.core.servers.restful_server import app
from app.core.servers import grpc_server


async def start_fastapi():
    config = uvicorn.Config(
        app=app,
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()


async def run():
    await asyncio.gather(
        start_fastapi(),
        # grpc_server.serve(),
    )
