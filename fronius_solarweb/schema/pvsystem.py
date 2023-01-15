from datetime import datetime
from typing import Any

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    zipCode: str
    city: str
    state: str
    country: str


class Status(BaseModel):
    isOnline: bool
    battMode: str


class PvSystemMetaData(BaseModel):
    pvSystemId: str
    name: str
    address: Address
    timezone: datetime
    pictureURL: str
    peakPower: float
    meteoData: str
    lastImport: datetime
    installationDate: datetime


class PvSystemFlowData(BaseModel):
    pvSystemId: str
    status: Status
    address: Address
    timezone: datetime
    pictureURL: str
    peakPower: float
    meteoData: str
    lastImport: datetime
    installationDate: datetime


class Channel(BaseModel):
    channelName: str
    channelType: str
    unit: str
    value: Any


class Data(BaseModel):
    logDateTime: datetime
    channels: Channel
