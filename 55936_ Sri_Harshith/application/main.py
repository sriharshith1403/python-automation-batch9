from api_client import fetch_users
from Validating import validate_response
from File_Handling import save_to_csv, save_to_json

url = "https://jsonplaceholder.typicode.com/users"

def run():
    response = fetch_users(url)
    users = validate_response (response)

    print(f"API request successful: {response.status_code} OK")
    print(f"Valid records processed {len(users)}")

    save_to_json ("users.json",users)
    save_to_csv ("users.csv",users)

    print("Data saved to users.json")
    print("Data saved to users.csv ")

if __name__ == "__main__":
    run()
