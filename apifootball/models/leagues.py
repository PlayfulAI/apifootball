from datetime import date
from typing import List

from pydantic import BaseModel

from .shared import ResponseWrapper


class LeagueDetails(BaseModel):
    id: int
    name: str
    type: str
    logo: str


class LeagueCountry(BaseModel):
    name: str
    code: str | None  # `None` when `name == "World"`.
    flag: str | None  # `None` when `name == "World"`.


class LeagueSeason(BaseModel):
    year: int
    start: date
    end: date
    current: bool
    coverage: dict


class League(BaseModel):
    league: LeagueDetails
    country: LeagueCountry
    seasons: List[LeagueSeason]


class LeaguesWrapper(ResponseWrapper):
    response: List[League]
