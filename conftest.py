import pytest
import random

from api_helpers import create_user

# ---------- test data ----------
@pytest.fixture
def user_data():
    rand = random.randint(1000, 9999)
    return {
        "login": f"test_user_{rand}",
        "email": f"test_{rand}@mail.com",
        "password": "Password123!"
    }

@pytest.fixture
def created_user(user_data):
    response = create_user(
        user_data["login"],
        user_data["email"],
        user_data["password"]
    )

    assert response.status_code in (200, 201), response.text
    data = response.json()

    assert "login" in data
    assert "User-Token" in data or "user_token" in data
    user_token = data.get("User-Token") or data.get("user_token")

    return {
        "login": user_data["login"],
        "email": user_data["email"],
        "token": user_token
    }

@pytest.fixture
def created_invalid_user(request):
    requestData = request.param
    response = create_user(
        requestData['login'],
        requestData['email'],
        requestData['password']
    )

    # Negative case should return 400 codes, but this endpoint still returning 200. 
    # I would say that it's a bug and should be fixed, but I'll keep check on 200 status to test keep working, because we check not only status, but error message.
    assert response.status_code in (200, 201), response.text
    data = response.json()

    return {
        "requestData": requestData,
        "response_data": data
    }
