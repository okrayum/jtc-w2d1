import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc

class Task4Service(service_pb2_grpc.Task4ServiceServicer):
  def SayHello(self, request, context):
    return service_pb2.HelloResponse(message=f"Hello, {request.name}!")
  
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  service_pb2_grpc.add_Task4ServiceServicer_to_server(Task4Service(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  print("Listening on port 500051...")
  server.wait_for_termination()

if __name__ == "__main__":
  serve()

