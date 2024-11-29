from typing import Optional, List

from pydantic import BaseModel


class PagingLinks(BaseModel):
    first: Optional[str]
    prev: Optional[str]
    self: Optional[str]
    next: Optional[str]
    last: Optional[str]
    totalItemsCount: int


class HistoricalChannel(BaseModel):
    channelName: Optional[str]
    channelType: Optional[str]
    unit: Optional[str]
    value: Optional[float]
    isActive: Optional[bool]
    isDamaged: Optional[bool]


class HistoricalData(BaseModel):
    logDateTime: Optional[str]
    logDuration: int
    channels: Optional[List[HistoricalChannel]]


class HistoricalValues(BaseModel):
    pvSystemId: Optional[str]
    deviceId: Optional[str]
    data: Optional[List[HistoricalData]]
    links: PagingLinks
    totalDataCount: int
