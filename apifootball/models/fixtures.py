from enum import Enum
from typing import Dict, List

from pydantic import AwareDatetime, BaseModel

from .shared import ResponseWrapper


class FixtureShortStatus(str, Enum):
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


class FixtureStatus(BaseModel):
    long: str
    short: FixtureShortStatus
    elapsed: int | None


class FixtureLeague(BaseModel):
    id: int
    name: str
    country: str
    logo: str
    flag: str
    season: int
    round: str


class FixtureTeam(BaseModel):
    id: int
    name: str
    logo: str
    winner: bool | None = None


class FixtureTeams(BaseModel):
    home: FixtureTeam
    away: FixtureTeam


class FixtureScore(BaseModel):
    home: int | None
    away: int | None


class FixturePlayer(BaseModel):
    id: int | None
    name: str | None


class FixtureEventType(str, Enum):
    goal = "Goal"
    card = "Card"
    subst = "subst"
    var = "Var"


class FixtureEventDetail(str, Enum):
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


class FixtureEvent(BaseModel):
    time: Dict[str, int | None]
    team: FixtureTeam
    player: FixturePlayer
    assist: FixturePlayer
    type: FixtureEventType
    detail: FixtureEventDetail
    comments: str | None


class FixtureVenue(BaseModel):
    id: int
    name: str
    city: str


class FixtureDetails(BaseModel):
    id: int
    referee: str | None
    timezone: str
    date: AwareDatetime
    timestamp: int
    periods: dict
    venue: FixtureVenue
    status: FixtureStatus


class Fixture(BaseModel):
    fixture: FixtureDetails
    league: FixtureLeague
    teams: FixtureTeams
    goals: FixtureScore
    score: Dict[str, FixtureScore]
    events: List[FixtureEvent] | None = None


class FixturesWrapper(ResponseWrapper):
    response: List[Fixture]
