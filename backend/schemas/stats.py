from pydantic import BaseModel

from typing import Optional

from datetime import date


class StatsCreate(BaseModel):
    date: date
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]


class StatsShow(BaseModel):
    from_date: date
    to_date: date

