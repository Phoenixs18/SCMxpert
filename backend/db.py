#establish connection between Python and Mongo

from pymongo import MongoClient

# myclient = MongoClient("mongodb://localhost:27017/")
myclient = MongoClient("mongodb+srv://Test:Test123@scmxpert.5zizz6x.mongodb.net/?retryWrites=true&w=majority")
db = myclient["SCMXpert"]
user_data=db["user"]
shipment_data=db["shipments"]
stream_data=db["Device_Data_Stream"]