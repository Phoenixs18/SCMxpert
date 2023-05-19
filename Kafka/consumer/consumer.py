# import json
# import sys
# from models import Device_Data
# from pymongo import MongoClient
# from kafka import KafkaConsumer

# # MongoClient(db="SCMXpert", host="localhost", port=27017)
# # client=MongoClient("mongodb://localhost:27017")
# # client=MongoClient("mongodb+srv://Test:Test123@scmxpert.5zizz6x.mongodb.net/?retryWrites=true&w=majority")

# username = "Test"
# password = "Test123"

# databaseurl = "mongodb+srv://{}:{}@scmxpert.5zizz6x.mongodb.net/?retryWrites=true&w=majority".format(username, password)

# # client=MongoClient(os.getenv("databaselocal"))
# client=MongoClient(databaseurl)
# db=client["SCMXpert"]
# stream_data=db["Device_Data_Stream"]

# bootstrap_servers = 'localhost:9092'

# # bootstrap_servers = "backend-kafka-1:9092"
# topic_name = 'device_data'



# try:
#     consumer = KafkaConsumer(topic_name, 
#                              bootstrap_servers = bootstrap_servers,
#                              auto_offset_reset = 'latest')
    
#     for data in consumer:
#         data = json.loads(data.value)
#         Transport_Data = Device_Data(
#             Battery_Level= data["Battery_Level"],
#             Device_ID= data["Device_ID"],
#             First_Sensor_Temperature= data["First_Sensor_Temperature"],
#             Route_From= data["Route_From"],
#             Route_To= data["Route_To"]
#         )
#         stream_data.insert_one(dict(Transport_Data))
#         print(Transport_Data)

# except KeyboardInterrupt:
#     sys.exit()

import json
from pathlib import Path
from mongoengine import connect
from kafka import KafkaConsumer
from pydantic import BaseModel
import sys
import models
import os
from dotenv import load_dotenv
import urllib.parse

from pymongo import MongoClient
# load_dotenv()

# base_dir = Path(__file__).resolve().parent

url = "mongodb+srv://Test:Test123@scmxpert.5zizz6x.mongodb.net/?retryWrites=true&w=majority"
client=MongoClient(url)

database=client["SCMXpert"]
Device_Data_Stream=database["Device_Data_Stream"]

bootstrap_servers = 'backend-kafka-1:9092'
# bootstrap_servers = 'root-kafka-1:9092'
# bootstrap_servers = 'localhost:9092'
topicName='Device_Data_Stream'

class Device_Data(BaseModel):
        Battery_Level: int
        Device_Id: int
        First_Sensor_temperature: int
        Route_From: str
        Route_To: str

try:
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')
    for data in consumer:
        data = json.loads(data.value)
        Transport_Data = models.Device_Data(
            Battery_Level = data['Battery_Level'],
            Device_Id = data['Device_ID'],
            First_Sensor_temperature = data['First_Sensor_Temperature'],
            Route_From = data['Route_From'],
            Route_To = data['Route_To']                        
        )
        
        Device_Data_Stream.insert_one(dict(Transport_Data))
        print(Transport_Data)
except KeyboardInterrupt:
    sys.exit()