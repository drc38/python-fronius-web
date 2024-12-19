from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .device import Links


class Address(BaseModel):
    street: Optional[str] = None
    zipCode: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None


class Channel(BaseModel):
    channelName: Optional[str] = None
    channelType: Optional[str] = None
    unit: Optional[str] = None
    value: Optional[float | str] = None


class Data(BaseModel):
    logDateTime: Optional[datetime] = None
    channels: Optional[list[Channel]] = None


class AggrData(BaseModel):
    logDateTime: Optional[str] = None
    channels: Optional[list[Channel]] = None


class EnergyFlowStatus(BaseModel):
    isOnline: bool
    battMode: Optional[float | str] = None


class PvSystemMetaData(BaseModel):
    pvSystemId: str
    name: Optional[str] = None
    address: Optional[Address] = None
    timezone: Optional[datetime] = None
    pictureURL: Optional[str] = None
    peakPower: Optional[float] = None
    meteoData: Optional[str] = None
    lastImport: Optional[datetime] = None
    installationDate: Optional[datetime] = None


class PvSystemsMetaData(BaseModel):
    pvSystems: Optional[list[PvSystemMetaData]] = None
    # Swagger documentation extras
    links: Optional[Links] = None


class PvSystemFlowData(BaseModel):
    pvSystemId: str
    status: Optional[EnergyFlowStatus] = None
    data: Optional[Data] = None


class PvSystemAggrDataV2(BaseModel):
    pvSystemId: str
    data: Optional[list[AggrData]] = None
    links: Optional[Links] = None
