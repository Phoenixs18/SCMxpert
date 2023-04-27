from pydantic import BaseModel ##to request body from user
from mongoengine import Document, StringField, IntField, DateField, DynamicDocument
#from fastapi import Query


class NewUser(BaseModel):
    username:str 
    email:str 
    password: str 


class UserInDB(NewUser):
    hashed_password: str

class Login(BaseModel):
    username:str 
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    username: str | None = None

class NewShipment(BaseModel):
    invoice_no: int
    container_no: int
    shipment_description: str
    route_details:str
    goods_type: str
    device: str  
    expected_delivery_date: str
    PO_number: str
    delivery_no: int
    NDC_no: int
    batch_id: int
    serial_no_of_goods: int


class DeviceData(DynamicDocument):
    battery_level = IntField()
    device_id = IntField()
    first_sensor_temperature = IntField()
    route_from = StringField()
    route_to = StringField()  


class User(Document):
    username=StringField()
    email=StringField()
    password=StringField()


class Shipments(Document):
    invoice_no = IntField()
    container_no = IntField()
    shipment_description = StringField()
    route_details = StringField()
    goods_type = StringField()
    device = StringField()
    expected_delivery_date = StringField()
    PO_number = StringField()
    delivery_no = IntField()
    NDC_no = IntField()
    batch_id = IntField()
    serial_no_of_goods = IntField()

