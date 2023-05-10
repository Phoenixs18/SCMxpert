import json
import sys
from models import Device_Data
from pymongo import MongoClient
from kafka import KafkaConsumer

client=MongoClient("mongodb://localhost:27017")
db=client["SCMXpert"]
col3=db["Device_Data_Stream"]

bootstrap_servers = "localhost:9092"
topic_name = 'device_data'


try:
    consumer = KafkaConsumer(topic_name, 
                             bootstrap_servers = bootstrap_servers,
                             auto_offset_reset = 'latest')
    
    for data in consumer:
        data = json.loads(data.value)
        Transport_Data = Device_Data(
            Battery_Level= data["Battery_Level"],
            Device_ID= data["Device_ID"],
            First_Sensor_Temperature= data["First_Sensor_Temperature"],
            Route_From= data["Route_From"],
            Route_To= data["Route_To"]
        )
        col3.insert_one(dict(Transport_Data))
        print(Transport_Data)

except KeyboardInterrupt:
    sys.exit()