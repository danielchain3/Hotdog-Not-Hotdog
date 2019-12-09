from concurrent import futures
import logging
import hashlib

import grpc

import hashing_pb2
import hashing_pb2_grpc

class ByteStreamHashing(hashing_pb2_grpc.ByteStreamHashingServicer):

    def Hashing (self, request, context):
        #store the orignal byte stream
        bs = request.photoByteStream

        #hash result
        result = hashlib.sha256(bs).hexdigest()
        
        return hashing_pb2.HashReply(hashedKey = result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hashing_pb2_grpc.add_ByteStreamHashingServicer_to_server(ByteStreamHashing(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

                
