from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Firmware(BaseModel):
    updateAvailable: Optional[bool] = None
    installedVersion: Optional[str] = None
    availableVersion: Optional[str] = None


class Links(BaseModel):
    first: Optional[str] = None
    prev: Optional[str] = None
    self: Optional[str] = None
    next: Optional[str] = None
    last: Optional[str] = None
    totalItemsCount: int


class Power(BaseModel):
    dc1: Optional[float] = None
    dc2: Optional[float] = None
    dc3: Optional[float] = None
    dc4: Optional[float] = None


class Sensor(BaseModel):
    sensorType: Optional[str] = None
    sensorName: Optional[str] = None
    isActive: Optional[bool] = None
    activationDate: Optional[datetime] = None
    deactivationDate: Optional[datetime] = None


class DeviceMetaData(BaseModel):
    # inverter
    deviceType: Optional[str] = None
    deviceId: str
    deviceName: Optional[str] = None
    deviceManufacturer: Optional[str] = None
    serialnumber: Optional[str] = None
    deviceTypeDetails: Optional[str] = None
    dataloggerId: Optional[str] = None
    nodeType: Optional[str] = None
    numberMPPTrackers: Optional[int] = None
    numberPhases: Optional[int] = None
    peakPower: Optional[Power] = None
    nominalAcPower: Optional[float] = None
    firmware: Optional[Firmware] = None
    isActive: Optional[bool] = None
    activationDate: Optional[datetime] = None
    deactivationDate: Optional[datetime] = None
    # battery extras
    capacity: Optional[float] = None
    # sensor extras
    sensors: Optional[Sensor] = None
    # smart meter extras
    deviceCategory: Optional[str] = None
    deviceLocation: Optional[str] = None
    # EV charger extras
    isOnline: Optional[bool] = None
    # Data logger extras
    # Swagger documentation extras
    ipAddressV4: Optional[str] = None


class DevicesMetaData(BaseModel):
    devices: Optional[list[DeviceMetaData]] = None
    # Swagger documentation extras
    links: Optional[Links] = None
