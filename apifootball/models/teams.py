from typing import List

from pydantic import BaseModel

from .shared import ResponseWrapper


class TeamVenue(BaseModel):
    id: int
    name: str
    address: str
    city: str
    capacity: int
    surface: str
    image: str


class TeamDetails(BaseModel):
    id: int
    name: str
    logo: str
    code: str | None
    country: str
    founded: int | None
    national: bool


class Team(BaseModel):
    team: TeamDetails
    venue: TeamVenue


class TeamsWrapper(ResponseWrapper):
    response: List[Team]
