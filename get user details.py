import requests
def get_user_details (username):
    url = f"https://api.github.com/users/(username)"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print("User Name:", user_data["login"])
        print("public repos:", user_data["public_repos"])

    else:
        print("Failed to fetch data")

        get_user_details("octocal")