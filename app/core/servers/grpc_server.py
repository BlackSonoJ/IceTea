import grpc

from app.generated.protos.schedule import schedule_pb2_grpc
from app.transports.protos.schedule.handler import ScheduleServer

from app.db.session import get_session


async def serve():
    server = grpc.aio.server()
    async with get_session() as session:
        schedule_pb2_grpc.add_ScheduleServerServicer_to_server(
            ScheduleServer(session), server
        )
        server.add_insecure_port("[::]:50051")
        await server.start()
        await server.wait_for_termination()
