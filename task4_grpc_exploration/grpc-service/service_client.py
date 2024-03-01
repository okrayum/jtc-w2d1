import grpc
import service_pb2
import service_pb2_grpc

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = service_pb2_grpc.Task4ServiceStub(channel)
  request = service_pb2.HelloRequest()
  request.name = "Jason"
  response = stub.SayHello(request)
  print("Server response:", response.message)

if __name__ == "__main__":
  run()
