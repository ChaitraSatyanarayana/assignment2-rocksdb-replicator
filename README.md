# The aim is to replicate the rocskdb database
Consists of 5 files attached: master.py, slave.py, replicate.proto, replicate_pb2.py replicate_pb2_grpc.py
Master runs on port 50051
The master will perform three operations on database : PUT UPDATE and DELETE 

#   PUT
Puts new value to the databases
Input : Value to store in database
Key will be geneted and displayed
The same value will be stored in slave database  as well as master database

#  UPDATE
Already existing value is replaced
Input : Value and Key 

# DELETE 
Deletes the value in database 
Input :Key 
Value and key will be deleted from the databases

# Pre-Requiistes:
 -> Python 3
 -> rocskdb 
 -> grpc
 
# OS : Linux Ubuntu 16.0.4

# Steps to Run 
# run the master:
      python3 master.py
      
# run the slave:(in another terminally)
      python3 slave.py
 #Enter the operation to be done (PUT , UPDATE or DELETE)     

 
