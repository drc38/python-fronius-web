from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Address(BaseModel):
    street: Optional[str]
    zipCode: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]

class Channel(BaseModel):
    channelName: Optional[str]
    channelType: Optional[str]
    unit: Optional[str]
    value: Optional[float | str]

class Data(BaseModel):
    logDateTime: Optional[datetime]
    channels: Optional[Channel]

class Status(BaseModel):
    isOnline: bool
    battMode: Optional[str]

class PvSystemMetaData(BaseModel):
    pvSystemId: str
    status: Optional[Status]
    address: Optional[Address]
    timezone: Optional[datetime]
    pictureURL: Optional[str]
    peakPower: Optional[float]
    meteoData: Optional[str]
    lastImport: Optional[datetime]
    installationDate: Optional[datetime]

class PvSystemFlowData(BaseModel):
    pvSystemId: str
    status: Optional[Status]
    data: Optional[Data]
    