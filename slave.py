import grpc
import replicate_pb2
import replicate_pb2_grpc
import rocksdb
import argparse
PORT = 3000;

slave_db = rocksdb.DB("test1.db", rocksdb.Options(create_if_missing=True))
keys =[]

class ReplicatorSlave():
   def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = replicate_pb2.ReplicateStub(self.channel)

   def connect_master(self, request):
        return self.stub.connect_master(replicate_pb2.Request(connect_request=request))

   def store(self,request):
       return self.stub.store(replicate_pb2.Store_Request(store_request=request))


def run():
    channel = grpc.insecure_channel('localhost:3000')
    stub = replicate_pb2_grpc.ReplicateStub(channel)
    response = stub.connect_master(replicate_pb2.Request(connect_request="Master Please Connect"))
    print("Master response is "+ response.connect_response)
    while(1):
        data = stub.store(replicate_pb2.Store_Request(store_request="Please send the store value and key"))
        if (data.operation == "PUT"):
            put(data.key,data.value)
        elif (data.opeartion =="UPDATE"):
            update(data.key,data.value)
        elif (data.opearion =="DELETE"):
            delete(data.key,data.value)
        else: print("Invalid syntax")

def put(key,value):
    print("It is put operation")
    print (key+" "+value)
    return

def update():
    print("It is update operation")
    print("Enter key: ")
    key = input()
    while key not in keys:
        print("key value not in database")
        print("Enter key: ")
        key = input()
    print("enter the value: ")
    value = input()
    key = key.encode('ASCII')
    value = value.encode('ASCII')
    print("Before: "+masterDB.get(key).decode())
    masterDB.put(key,value)
    print("After: "+masterDB.get(key).decode())
    return key


def delete():
    print("It is delete operation")
    print("Enter key: ")
    key = input()
    while key not in keys:
        print("Key not in database")
        print("Enter key: ")
        key = input()
    keys.remove(key)
    key = key.encode('ASCII')
    masterDB.delete(key)
    return key

if __name__=="__main__":
    run()

