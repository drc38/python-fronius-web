from typing import Optional, List

from pydantic import BaseModel


class PagingLinks(BaseModel):
    first: Optional[str] = None
    prev: Optional[str] = None
    self: Optional[str] = None
    next: Optional[str] = None
    last: Optional[str] = None
    totalItemsCount: int


class HistoricalChannel(BaseModel):
    channelName: Optional[str] = None
    channelType: Optional[str] = None
    unit: Optional[str] = None
    value: Optional[float] = None
    isActive: Optional[bool] = None
    isDamaged: Optional[bool] = None


class HistoricalData(BaseModel):
    logDateTime: Optional[str] = None
    logDuration: int
    channels: Optional[List[HistoricalChannel]] = None


class HistoricalValues(BaseModel):
    pvSystemId: Optional[str] = None
    deviceId: Optional[str] = None
    data: Optional[List[HistoricalData]] = None
    links: PagingLinks
    totalDataCount: Optional[int] = None
