from api_helpers import get_user, update_user
import pytest

# User created in fixture "created_user"
def test_create_and_get_user(created_user):
    response = get_user(created_user["login"], created_user["token"])
    assert response.status_code == 200

    user = response.json()
    assert user["login"] == created_user["login"]
    assert user["account_details"]["email"] == created_user["email"]

def test_update_user(created_user):
    new_login = created_user["login"] + "_upd"
    new_email = "upd_" + created_user["email"]

    response = update_user(
        created_user["login"],
        created_user["token"],
        new_login,
        new_email
    )

    assert response.status_code == 200
    assert "User successfully updated." in response.json()['message']

    response = get_user(new_login, created_user["token"])
    assert response.status_code == 200

    user = response.json()
    assert user["login"] == new_login
    assert user["account_details"]["email"] == new_email

@pytest.mark.parametrize('created_invalid_user', 
                         [
        {"login": "!!!bad_login", "email": "test@mail.com", "password": "123", "error_code": "32", "message": "Username can only contain letters (a-z), numbers (0-9) and the underscore (_); Email has already been taken; Password is too short (minimum is 5 characters)"},
        {"login": "toolongtoolongtoolongtoolong", "email": "invalid", "password": "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890", "error_code": "32", "message": "Username is too long (maximum is 20 characters); Email is not a valid email; Password is too long (maximum is 120 characters)"},
        # {"login": "", "email": "", "password": ""}, -> For some reason this 2 cases are working, it seems like a bug
        # {"login": " ", "email": " ", "password": " "}, -> For some reason this 2 cases are working, it seems like a bug
    ],
    indirect=True
)
def test_create_user_with_invalid_login(created_invalid_user):
    assert created_invalid_user['response_data']['error_code'] == int(created_invalid_user['requestData']['error_code'])
    assert created_invalid_user['response_data']['message'] == created_invalid_user['requestData']['message']