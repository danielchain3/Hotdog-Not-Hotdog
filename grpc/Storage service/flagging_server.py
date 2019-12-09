from concurrent import futures
import logging
import redis

import grpc

import flagging_pb2
import flagging_pb2_grpc

DB_ADD = '10.107.212.83'
class PhotoFlagging(flagging_pb2_grpc.PhotoFlaggingServicer):

    def UserSubmit(self, request, context):
        ##create connection to redis database
        r = redis.Redis(host=DB_ADD, port=6379, db=0)

        ##nameSpace for user-hash keyvalue
        NSHASH = 'hashs:'
        NSUSERHASH = 'user-hash:'

        ## get info from request
        userid = request.userId
        hashKey = request.hashKey

        ##initialization of return values
        reject = False
        exist = False

        ## check if the hash exist
        if r.exists(NSHASH + hashKey) > 0:
            exist = True
            reject = (r.get(NSHASH + hashKey) == '1')
        ## if the hash does not exist in the database
        else:
            exist = False
            reject = False

            ##add the hash to database
            r.set(NSHASH + hashKey, 0)

        ##modify or add to the user-hash list
        r.sadd(NSUSERHASH + userid, hashKey)
        
        return flagging_pb2.UserSubmitReply(rejected = reject, existed = exist)


    def UserRequest(self, request, context):
        ##create connection to redis database
        r = redis.Redis(host=DB_ADD, port=6379, db=0)

        ##nameSpace for user-hash keyvalue
        NSHASH = 'hashs:'
        NSUSERHASH = 'user-hash:'

        ## get all unflagged photo hash of a user
        resultList = []
        hashList = list(r.smembers(NSUSERHASH + request.userId))
        for h in hashList:
            if r.get(NSHASH + h) == '0':
                resultList += [h]

        return flagging_pb2.UserRequestReply(unflaggedHash = resultList)


    def AdminSubmit(self, request, context):
        ##create connection to redis database
        r = redis.Redis(host=DB_ADD, port=6379, db=0)

        ##nameSpace for user-hash keyvalue
        NSHASH = 'hashs:'
        NSUSERHASH = 'user-hash:'

        ## get info from request
        hashKey = request.hashKey

        ## initalization of result list
        hashList = []
        flagList = []

        ## set or remove the flag
        curFlag = int(r.get(NSHASH + hashKey))
        r.set(NSHASH + hashKey, 1 - curFlag)

        """
        ## update all the users' user-hash list
        curFlag = int(r.get(NSHASH + hashKey))
        ## if flag is set
        if curFlag == 1:
            for u in r.scan_iter(match = NSUSERHASH + '*'):
                if r.sismember(u, hashKey):
                    r.srem(u, hashKey)
        
        ## if flag is removed
        if curFlag == 0:
            for u in r.scan_iter(match = NSUSERHASH + '*'):
                if r.sismember(u, hashKey):
                    r.sadd(u, hashKey)
        """
        
        ##fetch updated result
        hashList = r.keys(NSHASH + '*')
        flagList = r.mget(hashList)
        flagList = [f == '1' for f in flagList]
        hashList = [s[6:] for s in hashList]

        return flagging_pb2.AdminSubmitReply(hashKeyList = hashList, flaggedList = flagList)

    
    def AdminRequest(self, request, context):
        ##create connection to redis database
        r = redis.Redis(host=DB_ADD, port=6379, db=0)

        ##nameSpace for user-hash keyvalue
        NSHASH = 'hashs:'
        NSUSERHASH = 'user-hash:'

        ## get info from request
        userid = request.userId

        ## initalization of result list
        hashList = []
        flagList = []

        ## if no userid is left blank
        if userid == '' or userid is None:
            ##get all hashes
            hashList = r.keys(NSHASH + '*')
            flagList = r.mget(hashList)
            flagList = [f == '1' for f in flagList]
            hashList = [s[6:] for s in hashList]
        ## if a userid is specified
        else:
            ##get all hashes of the user
            hashList = r.smembers(NSUSERHASH + userid)
            tempGetList = [NSHASH + s for s in hashList]
            flagList = r.mget(tempGetList)
            flagList = [f == '1' for f in flagList]

        return flagging_pb2.AdminRequestReply(hashKeyList = hashList, flaggedList = flagList)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    flagging_pb2_grpc.add_PhotoFlaggingServicer_to_server(PhotoFlagging(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

                
