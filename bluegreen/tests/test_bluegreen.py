import pytest
from app.index import app

@pytest.fixture
def client():
    client = app.test_client()

    yield client

def test_200(client):
    response = client.get('/')
    assert response.status_code == 200

def test_color(client):
    response = client.get('/')
    assert b"Undefined" in response.data