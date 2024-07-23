from datetime import date, datetime, timezone

import pytest
from tutils import patch_get  # noqa: F401

from apifootball import APIFootballClient


@pytest.fixture
def client(patch_get):  # noqa: F811
    return APIFootballClient(key="DUMMY")


def test_get_fixtures_by_date_range(client):
    res = client.get_fixtures(
        league=61,
        season=2022,
        from_=date(2022, 8, 5),
        to=date(2022, 8, 10),
    )
    assert len(res.response) == 10
    assert res.response[4].fixture.id == 871474
    assert res.response[4].goals.home == 2
    assert res.response[4].goals.away == 1


def test_get_fixtures_by_id(client):
    idx = 871470
    res = client.get_fixtures(idx)
    assert res.response[0].fixture.id == idx
    assert res.response[0].fixture.date == datetime(
        2022, 8, 6, 15, 0, 0, tzinfo=timezone.utc
    )
    assert res.response[0].score["fulltime"].home == 1
    assert res.response[0].score["fulltime"].away == 2


def test_get_teams_by_season(client):
    res = client.get_teams(league=39, season=2010)
    assert len(res.response) == 20
    assert res.response[2].team.id == 36
    assert res.response[2].team.name == "Fulham"
    assert res.response[2].venue.address == "Stevenage Road"
    assert res.response[2].venue.capacity == 25700


def test_get_leagues_by_code(client):
    res = client.get_leagues(code="lu")
    assert len(res.response) == 2
    assert res.response[0].league.id == 261
    assert len(res.response[1].seasons) == 4
    assert res.response[1].seasons[2].start == date(2022, 9, 9)
    assert res.response[1].country.name == "Luxembourg"
