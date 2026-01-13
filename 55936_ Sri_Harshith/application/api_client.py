import requests


def fetch_users(url):
    try:
        response = requests.get(url,timeout=5)
        return response
    except requests.RequestException as e:
        raise RuntimeError(f"API error: {e}")