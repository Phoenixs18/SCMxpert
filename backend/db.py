#establish connection between Python and Mongo

from pymongo import MongoClient
from mongoengine import  connect ##to connect to mongodb
from fastapi import FastAPI
#connection_string="mongodb://localhost:27017"
#client=MongoClient(connection_string)


# #Creating DB
# db=client["SCMXpert"]

# #Creating collections
# collection_name=db.create_collection("newuser")
# collection_shipment=db.create_collection("shipmentdetails")
# collection_device=db.create_collection("device_data")


# app=FastAPI()
# client = connect(db="SCMXpert", host="localhost", port=27017)#username,#password) ##if authentication is provided

# collection_name = client["newuser"]
# collection_shipment = client["shipmentdetails"]
# collection_device=client["device_data"]
