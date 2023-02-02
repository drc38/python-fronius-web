from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Firmware(BaseModel):
    updateAvailable: Optional[bool]
    installedVersion: Optional[str]
    availableVersion: Optional[str]

class Links(BaseModel):
    first: Optional[str]
    prev: Optional[str]
    self: Optional[str]
    next: Optional[str]
    last: Optional[str]
    totalItemsCount: int

class Power(BaseModel):
    dc1: Optional[float] 
    dc2: Optional[float] 
    dc3: Optional[float] 
    dc4: Optional[float] 

class Sensor(BaseModel):
    sensorType: Optional[str]
    sensorName: Optional[str]
    isActive: Optional[bool]
    activationDate: Optional[datetime]
    deactivationDate: Optional[datetime] 


class DeviceMetaData(BaseModel):
    # inverter
    deviceType: Optional[str]
    deviceId: str
    deviceName: Optional[str]
    deviceManufacturer: Optional[str]
    serialnumber: Optional[str]
    deviceTypeDetails: Optional[str] 
    dataloggerId: Optional[str]
    nodeType: Optional[str] 
    numberMPPTrackers: Optional[int] 
    numberPhases: Optional[int] 
    peakPower: Optional[Power] 
    nominalAcPower: Optional[float] 
    firmware: Optional[Firmware] 
    isActive: Optional[bool]
    activationDate: Optional[datetime]
    deactivationDate: Optional[datetime] 
    # battery extras
    capacity: Optional[float] 
    # sensor extras
    sensors: Optional[Sensor] 
    # smart meter extras
    deviceCategory: Optional[str] 
    deviceLocation: Optional[str] 
    # EV charger extras
    isOnline: Optional[bool] 
    # Data logger extras
    # Swagger documentation extras
    ipAddressV4: Optional[str] 


class DevicesMetaData(BaseModel):
    devices: Optional[list[DeviceMetaData]]
    # Swagger documentation extras
    links: Optional[Links]
