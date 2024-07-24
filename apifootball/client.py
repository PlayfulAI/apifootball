from datetime import date
from typing import Optional

import requests
from pydantic import validate_call

from .models import FixturesWrapper, LeaguesWrapper, TeamsWrapper

ENDPOINT = "https://api-football-v1.p.rapidapi.com/v3"


class APIFootballSession(requests.Session):

    def __init__(self, key, endpoint):
        super().__init__()
        self.endpoint = endpoint
        self.headers.update({"x-rapidapi-key": key})

    def request(self, method, suffix, *args, **kwargs):
        url = self.endpoint + suffix
        return super().request(method, url, *args, **kwargs)


class APIFootballClient:

    def __init__(self, key, endpoint=ENDPOINT):
        self.sess = APIFootballSession(key, endpoint)

    @validate_call
    def get_fixtures(
        self,
        id_: Optional[int] = None,
        league: Optional[int] = None,
        season: Optional[int] = None,
        from_: Optional[date] = None,
        to: Optional[date] = None,
    ) -> FixturesWrapper:
        """Get fixtures."""
        params = dict()
        if id_ is not None:
            params["id"] = id_
        if league is not None:
            params["league"] = league
        if season is not None:
            params["season"] = season
        if from_ is not None:
            params["from"] = "{:%Y-%m-%d}".format(from_)
        if to is not None:
            params["to"] = "{:%Y-%m-%d}".format(to)
        res = self.sess.get("/fixtures", params=params)
        return FixturesWrapper.model_validate_json(res.text)

    @validate_call
    def get_teams(
        self,
        id_: Optional[int] = None,
        league: Optional[int] = None,
        season: Optional[int] = None,
    ) -> TeamsWrapper:
        """Get teams."""
        params = dict()
        if id_ is not None:
            params["id"] = id_
        if league is not None:
            params["league"] = league
        if season is not None:
            params["season"] = season
        res = self.sess.get("/teams", params=params)
        return TeamsWrapper.model_validate_json(res.text)

    @validate_call
    def get_leagues(
        self,
        code: Optional[str],
    ) -> LeaguesWrapper:
        """Get leagues."""
        params = dict()
        if code is not None:
            params["code"] = code
        res = self.sess.get("/leagues", params=params)
        return LeaguesWrapper.model_validate_json(res.text)
