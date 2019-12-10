from __future__ import print_function
import logging

import sys

import grpc

import hashing_pb2
import hashing_pb2_grpc


def run_hashing(bs):
    with grpc.insecure_channel('0.0.0.0:50052') as channel:
        stub = hashing_pb2_grpc.ByteStreamHashingStub(channel)
        response = stub.Hashing(hashing_pb2.HashRequest(photoByteStream = bs))
        return response.hashedKey



##only for testing purpose
if __name__ == '__main__':
    logging.basicConfig()
    
    ##command line input
    cli = ''

    ##hashed result
    hr = ''

    while cli != 'quit':
        cli = str(input('enter a string that you want to hash or quit: '))
        if (cli != 'quit'):
            hr = run_hashing(cli)
            print("result: " + hr)



