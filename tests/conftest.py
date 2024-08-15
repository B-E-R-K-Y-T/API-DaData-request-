import pytest
import requests

from src.config import settings


@pytest.fixture(scope="session")
def client():
    return requests.request


@pytest.fixture(scope="session")
def base_url():
    return settings.BASE_URL
