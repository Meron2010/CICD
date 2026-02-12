import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # Exempel-API

def test_get_posts_status_code():
    """Testar att GET /posts returnerar 200 OK"""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_single_post():
    """Testar att GET /posts/1 returnerar korrekt data"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == 1
    assert "title" in data

def test_create_post():
    """Testar att POST /posts returnerar 201 Created"""
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
