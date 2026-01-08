from api_client import fetch_users
from validator import validate_response
from file_handler import save_to_json, save_to_csv

URL = "https://jsonplaceholder.typicode.com/users"

def run():
    response = fetch_users(URL)
    users = validate_response(response)

    print(f"API request successful: {response.status_code} OK")
    print(f"Valid records processed: {len(users)}")

    save_to_json("users.json", users)
    save_to_csv("users.csv", users)

    print("Data saved to users.json")
    print("Data saved to users.csv")

if __name__ == "__main__":
    run()
