from __future__ import print_function
import logging

import sys

import grpc

import flagging_pb2
import flagging_pb2_grpc


def runUserSubmit(uid, hk):
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        stub = flagging_pb2_grpc.PhotoFlaggingStub(channel)
        response = stub.UserSubmit(flagging_pb2.UserSubmitRequest(userId = uid, hashKey = hk))
        result = {
            'rejected': response.rejected,
            'existed': response.existed
        }
        return result


def runUserRequest(uid):
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        stub = flagging_pb2_grpc.PhotoFlaggingStub(channel)
        response = stub.UserRequest(flagging_pb2.UserRequestRequest(userId = uid))
        return response.unflaggedHash


def runAdminSubmit(hk):
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        stub = flagging_pb2_grpc.PhotoFlaggingStub(channel)
        response = stub.AdminSubmit(flagging_pb2.AdminSubmitRequest(hashKey = hk))
        result = {}
        ##create the output dictionary hash is the key, flag is the value
        for h, f in zip(response.hashKeyList, response.flaggedList):
            result[h] = f
        return result

def runAdminRequest(uid):
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        stub = flagging_pb2_grpc.PhotoFlaggingStub(channel)
        response = stub.AdminRequest(flagging_pb2.AdminRequestRequest(userId = uid))
        result = {}
        ##create the output dictionary hash is the key, flag is the value
        for h, f in zip(response.hashKeyList, response.flaggedList):
            result[h] = f
        return result




"""
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
"""


