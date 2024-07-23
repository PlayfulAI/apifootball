from datetime import date
from enum import Enum
from typing import Any, Dict, List

from pydantic import AwareDatetime, BaseModel


class Venue(BaseModel):
    id: int
    name: str
    city: str


class ShortStatusEnum(str, Enum):
    # Scheduled
    tbd = "TBD"  # Scheduled but date and time are not known
    ns = "NS"  # Not Started
    # In play
    _1h = "1H"  # First half in play
    ht = "HT"  # Halftime
    _2h = "2H"  # Second half in play
    et = "ET"  # Extra time in play
    bt = "BT"  # Break during extra time
    p = "P"  # Penalties played after extra time
    susp = "SUSP"  # Suspended by referee's decision, may be rescheduled another day
    int_ = "INT"  # Interrupted by referee's decision, should resume in a few minutes
    live = "LIVE"  # In progress, used in very rare cases.
    # Finished
    ft = "FT"  # Finished in the regular time
    aet = "AET"  # Finished after extra time without going to the penalty shootout
    pen = "PEN"  # Finished after the penalty shootout
    # Other
    pst = "PST"  # Postponed to another day
    canc = "CANC"  # Cancelled, match will not be played
    abd = "ABD"  # Abandoned for various reasons
    awd = "AWD"  # Technical loss
    wo = "WO"  # Walkover, victory by forfeit or absence of competitor


class Status(BaseModel):
    long: str
    short: ShortStatusEnum
    elapsed: int | None


class FixtureDetails(BaseModel):
    id: int
    referee: str | None
    timezone: str
    date: AwareDatetime
    timestamp: int
    periods: dict
    venue: Venue
    status: Status


class League(BaseModel):
    id: int
    name: str
    country: str
    logo: str
    flag: str
    season: int
    round: str


class TeamDetails(BaseModel):
    id: int
    name: str
    logo: str
    winner: bool | None = None


class TeamDetailsExtended(TeamDetails):
    code: str
    country: str
    founded: int
    national: bool


class Teams(BaseModel):
    home: TeamDetails
    away: TeamDetails


class Score(BaseModel):
    home: int | None
    away: int | None


class Player(BaseModel):
    id: int | None
    name: str | None


class EventTypeEnum(str, Enum):
    goal = "Goal"
    card = "Card"
    subst = "subst"
    var = "Var"


class EventDetailEnum(str, Enum):
    # Type 'Goal'.
    normal_goal = "Normal Goal"
    own_goal = "Own Goal"
    penalty = "Penalty"
    missed_penalty = "Missed Penalty"
    # Type 'Card'.
    yellow_card = "Yellow Card"
    red_card = "Red Card"
    # Type 'Subst'
    substitution_1 = "Substitution 1"
    substitution_2 = "Substitution 2"
    substitution_3 = "Substitution 3"
    substitution_4 = "Substitution 4"
    substitution_5 = "Substitution 5"
    substitution_6 = "Substitution 6"
    substitution_7 = "Substitution 7"
    substitution_8 = "Substitution 8"
    # Type 'Var'
    goal_cancelled = "Goal cancelled"
    penalty_confirmed = "Penalty confirmed"


class Event(BaseModel):
    time: Dict[str, int | None]
    team: TeamDetails
    player: Player
    assist: Player
    type: EventTypeEnum
    detail: EventDetailEnum
    comments: str | None


class Fixture(BaseModel):
    fixture: FixtureDetails
    league: League
    teams: Teams
    goals: Score
    score: Dict[str, Score]
    events: List[Event] | None = None


class BaseWrapper(BaseModel):
    get: str
    parameters: Dict[str, Any]
    errors: list
    results: int
    paging: Dict[str, int]


class FixturesWrapper(BaseWrapper):
    response: List[Fixture]


class Venue(BaseModel):
    id: int
    name: str
    address: str
    city: str
    capacity: int
    surface: str
    image: str


class Team(BaseModel):
    team: TeamDetailsExtended
    venue: Venue


class TeamsWrapper(BaseWrapper):
    response: List[Team]


class LeagueDetails(BaseModel):
    id: int
    name: str
    type: str
    logo: str


class Country(BaseModel):
    name: str
    code: str
    flag: str


class Season(BaseModel):
    year: int
    start: date
    end: date
    current: bool
    coverage: dict


class League(BaseModel):
    league: LeagueDetails
    country: Country
    seasons: List[Season]


class LeaguesWrapper(BaseWrapper):
    response: List[League]
