import grpc

from generated.protos.schedule import schedule_pb2_grpc
from src.grpc_handlers.schedule_handler import ScheduleServer
from src.database import get_session


async def serve():
    server = grpc.aio.server()
    async with get_session() as session:
        schedule_pb2_grpc.add_ScheduleServerServicer_to_server(
            ScheduleServer(session), server
        )
        server.add_insecure_port("[::]:50051")
        await server.start()
        await server.wait_for_termination()
