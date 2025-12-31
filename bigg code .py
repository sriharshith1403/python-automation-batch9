import requests
url = "https://api.github"
response = requests.get(url)

print("--- HTTP RESPONSE DETAILS---")
print("status code:", response.status_code)
print("Response Headers:")
for key, value in response.headers.items():
    print(f"{key}:{value}")

    print("\nResponse Body:")
    print(response.text)