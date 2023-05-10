from pydantic import BaseModel

class Device_Data(BaseModel):
    Battery_Level: int
    Device_ID: int
    First_Sensor_Temperature: int
    Route_From: str
    Route_To: str
