def is_valid_user(user):
    return all(field in user and user[field] for field in ("id", "name", "email"))

def validate_response(response):
    if response.status_code != 200:
        raise ValueError("Invalid status code")

    if "application/json" not in response.headers.get("Content-Type", ""):
        raise ValueError("Invalid content type")

    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Invalid JSON structure")

    valid_users = [u for u in data if is_valid_user(u)]
    return valid_users
