from typing import List

from pydantic import BaseModel

from .shared import ResponseWrapper


class TeamVenue(BaseModel):
    id: int | None
    name: str | None
    address: str | None
    city: str | None
    capacity: int | None
    surface: str | None
    image: str | None


class TeamDetails(BaseModel):
    id: int
    name: str
    logo: str
    code: str | None
    country: str | None
    founded: int | None
    national: bool


class Team(BaseModel):
    team: TeamDetails
    venue: TeamVenue


class TeamsWrapper(ResponseWrapper):
    response: List[Team]
