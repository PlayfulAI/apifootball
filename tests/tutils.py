import hashlib
import os.path

import pytest
import requests  # noqa: F401

from apifootball.client import APIFootballSession

DATA_ROOT = os.path.join(os.path.dirname(__file__), "data")


class MockResponse:

    def __init__(self, text):
        self.text = text


def mock_get(self, url, **kwargs):
    d = make_digest(url, kwargs.get("params", {}))
    with open(os.path.join(DATA_ROOT, "{}.json".format(d)), "rb") as f:
        return MockResponse(f.read())


@pytest.fixture
def patch_get(monkeypatch):
    # Prevent any external request.
    monkeypatch.delattr("requests.sessions.Session.request")
    # Patch the `GET` method.
    monkeypatch.setattr(APIFootballSession, "get", mock_get)


def make_digest(url, data):
    s = str(url)
    for key, val in sorted(data.items()):
        s += str(key) + str(val)
    return hashlib.md5(s.encode()).hexdigest()[:16]
