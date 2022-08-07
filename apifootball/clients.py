from datetime import date
import requests


ENDPOINT = "https://api-football-v1.p.rapidapi.com/v3/"


class Client:

    def __init__(self, key, endpoint=ENDPOINT):
        self._key = key
        self._endpoint = endpoint

    def get_matches(self, league, season, date_from=None, date_to=None):
        """Get matches for a given league and season."""
        params = {
            "league": league,
            "season": season,
        }
        if date_from is not None:
            params["from"] = "{:%Y-%m-%d}".format(date_from)
        if date_to is not None:
            params["to"] = "{:%Y-%m-%d}".format(date_to)
        return self._get("fixtures", **params)["response"]
        
    def get_match(self, match_id):
        """Get match details."""
        return self._get("fixtures", id=match_id)["response"][0]

    def get_odds(self, league, season, bet=1, page=1):
        """Get bookmakers' odds for a match."""
        params = {
            "league": league,
            "season": season,
            "bet": bet,  # The bet with ID 1 is the usual 1x2 bet.
            "page": page,
        }
        res = self._get("odds", **params)
        return (res["paging"]["total"], res["response"])

    def _get(self, method, **params):
        headers = {"x-rapidapi-key": self._key}
        url = "{}/{}".format(self._endpoint, method)
        res = requests.get(url, headers=headers, params=params)
        return res.json()
