import requests, os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://favqs.com/api"

API_KEY = os.getenv("API_KEY")

HEADERS = {
    "Authorization": f'Token token="{API_KEY}"',
    "Content-Type": "application/json"
}

def create_user(login, email, password):
    url = f"{BASE_URL}/users"
    payload = {
        "user": {
            "login": login,
            "email": email,
            "password": password
        }
    }
    
    return requests.post(url, json=payload, headers=HEADERS)


def get_user(login, user_token):
    url = f"{BASE_URL}/users/{login}"
    headers = HEADERS.copy()
    headers["User-Token"] = user_token

    return requests.get(url, headers=headers)


def update_user(login, user_token, new_login, new_email):
    url = f"{BASE_URL}/users/{login}"

    headers = HEADERS.copy()
    headers["User-Token"] = user_token

    payload = {
        "user": {
            "login": new_login,
            "email": new_email
        }
    }

    return requests.put(url, json=payload, headers=headers)