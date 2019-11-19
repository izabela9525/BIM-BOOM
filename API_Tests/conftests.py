import os
import uuid
from datetime import datetime, timedelta

import pytest
import requests

@pytest.fixture(scope="session")
def authorized_user_headers():
    API_URL = f"https://test.bimstreamer.com/bim-server-tst/"
    token = requests.post(
        API_URL, headers={'Content-Type': 'application/x-www-form-urlencoded'},
        json={
            "grant_type": "password",
            "password": "jsnow",
            "username": "jsnow@example.com"
        }
    ).json()["access_token"]
    return {
        "Authorization": f"Bearer {token}"
    }