import rocksdb
from random import *
import replicate_pb2
import replicate_pb2_grpc
import grpc
from concurrent import futures


masterDB = rocksdb.DB("test.db", rocksdb.Options(create_if_missing=True))
keys =[]


class Replicate(replicate_pb2_grpc.ReplicateServicer):
    def __init__(self,f):
        self.f =f

    def __call__(self):
        print("in wrapper function:Call")
        self.key = self.f()
        self.value = masterDB.get(self.key)
        print ("key in wrapper is "+ self.key.decode())
        print("value in wrapper is "+self.value.decode())


    def connect_master(self,request,context):
         return replicate_pb2_grpc.Response(connect_response="Connected")

    def store(self,request,context):
        return replicate_pb2_grpc.Data(operation=self.f,key=self.key,value=self.value)

@Replicate
def put():
    print("It is put operation")
    key= randint(1,10000000000)
    while key in keys:
        key = randint(1,10000000000)
    key = str(key)
    keys.append(key)
    print("Enter the value: ")
    value = input()
    print("Key is : "+key)
    key = key.encode('ASCII')
    value = value.encode('ASCII')
    masterDB.put(key,value)
    print(masterDB.get(key))
    return key

@Replicate
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

@Replicate
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

def ip():
   while(1):
       print("Server waiting...")
       print("Please specify any of the operaions: PUT UPDATE DELETE")
       operation =input()
       print("Specified input is "+ operation)
       if(operation=="PUT"):
           put()
       elif(operation=="UPDATE"):
           update()
       elif(operation=="DELETE"):
           delete()
       else:
           print("invalid operation")


def run(host,port):
    #server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    #replicate_pb2_grpc.add_ReplicateServicer_to_server(Replicate(), server)
    #server.add_insecure_port('%s:%d' % (host, port))
    print("Server started at...%d" % port)
    while(1):
       print("Server waiting...")
       print("Please specify any of the operaions: PUT UPDATE DELETE")
       operation =input()
       print("Specified input is "+ operation)
       if(operation=="PUT"):
           put()
       elif(operation=="UPDATE"):
           update()
       elif(operation=="DELETE"):
           delete()
       else:
           print("invalid operation")
       server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
       replicate_pb2_grpc.add_ReplicateServicer_to_server(Replicate(operation), server)
       server.add_insecure_port('%s:%d' % (host, port))
       server.start()




if __name__ == '__main__':
    run('0.0.0.0', 3000)

