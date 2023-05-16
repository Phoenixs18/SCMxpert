#establish connection between Python and Mongo

from pymongo import MongoClient


myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["SCMXpert"]
user_data=db["user"]
shipment_data=db["shipments"]
stream_data=db["Device_Data_Stream"]