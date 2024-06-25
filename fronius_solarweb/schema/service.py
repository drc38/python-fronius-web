from typing import Optional

from pydantic import BaseModel


class ReleaseInfo(BaseModel):
    releaseVersion: Optional[str] = None
    releaseDate: Optional[str] = None
