import pytest
from datetime import datetime, date

from tutils import patch_get
from apifootball import Client


@pytest.fixture
def client(patch_get):
    return Client(key="DUMMY")


def test_get_matches(client):
    res = client.get_matches(
        league=61,
        season=2022,
        date_from=date(2022, 8, 5),
        date_to=date(2022, 8, 10),
    )
    assert len(res) == 10
    assert res[4]["fixture"]["id"] == 871474
    assert res[4]["goals"] == {
        "home": 2,
        "away": 1,
    }


def test_get_match(client):
    idx = 871470
    res = client.get_match(idx)
    assert res["fixture"]["id"] == idx
    assert res["fixture"]["date"] == "2022-08-06T15:00:00+00:00"
    assert res["score"]["fulltime"] == {
        "home": 1,
        "away": 2,
    }


def test_get_odds(client):
    idx = 178548
    n_pages, res = client.get_odds(league=61, season=2022)
    assert n_pages == 2
    assert len(res) == 10
    assert res[2]["update"] == "2022-08-06T16:02:44+00:00"
    assert res[2]["bookmakers"][1] == {
        "id": 27,
        "name": "NordicBet",
        "bets": [{
            "id": 1,
            "name": "Match Winner",
            "values": [
                {"value": "Home", "odd": "12.50"},
                {"value": "Draw", "odd": "6.40"},
                {"value": "Away", "odd": "1.23"},
            ]
        }],
    }
