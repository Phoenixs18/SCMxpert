from pydantic import BaseModel

class Device_Data(BaseModel):
    Battery_Level: int
    Device_Id: int
    First_Sensor_temperature: int
    Route_From: str
    Route_To: str
