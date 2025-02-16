import pytest
from weekThree.api_client import APIClient
import requests
from requests.exceptions import RequestException

def test_fetch_data_success(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def raise_for_status(self): pass
            text = "mock data"
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    client = APIClient("http://fakeurl.com")
    assert client.fetch_data() == "mock data"

def test_fetch_data_failure(monkeypatch):
    def mock_get(*args, **kwargs):
        raise RequestException("Error")
    monkeypatch.setattr(requests, "get", mock_get)
    client = APIClient("http://fakeurl.com")
    assert client.fetch_data() == ""