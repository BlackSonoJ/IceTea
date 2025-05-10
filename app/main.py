import asyncio

import uvicorn

from app.servers import fastapi_server, grpc_server


async def start_fastapi():
    config = uvicorn.Config(
        app=fastapi_server.app,
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    await asyncio.gather(
        start_fastapi(),
        grpc_server.serve(),
    )


if __name__ == "__main__":
    asyncio.run(main())
