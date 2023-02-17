from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .device import Links


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
    channels: Optional[list[Channel]]


class AggrData(BaseModel):
    logDateTime: Optional[str]
    channels: Optional[list[Channel]]


class Status(BaseModel):
    isOnline: bool
    battMode: Optional[str]


class PvSystemMetaData(BaseModel):
    pvSystemId: str
    name: Optional[str]
    status: Optional[Status]
    address: Optional[Address]
    timezone: Optional[datetime]
    pictureURL: Optional[str]
    peakPower: Optional[float]
    meteoData: Optional[str]
    lastImport: Optional[datetime]
    installationDate: Optional[datetime]


class PvSystemsMetaData(BaseModel):
    pvSystems: Optional[list[PvSystemMetaData]]
    # Swagger documentation extras
    links: Optional[Links]


class PvSystemFlowData(BaseModel):
    pvSystemId: str
    status: Optional[Status]
    data: Optional[Data]


class PvSystemAggrDataV2(BaseModel):
    pvSystemId: str
    data: Optional[list[AggrData]]
    links: Optional[Links]
