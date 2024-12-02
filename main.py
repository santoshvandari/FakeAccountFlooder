import json
import urllib.parse
import base64
import requests
from faker import Faker

# Create a Faker instance for generating fake data
fake = Faker()

# URL where the data is to be posted
URL = "https://lerih3.cc/api/user/register"
I = 0


def phone_number():
    # Generate a random phone number starting with 98
    random_int = fake.random_int(min=10000000, max=99999999)
    phone_number = f"98{random_int}"
    return phone_number

def generate_data():
    # Generate data in the required JSON format
    data_dict = {
        "username": phone_number(),
        "mobile": phone_number(),
        "password": fake.password(),
        "inviter": "314805",
        "machine": str(fake.random_int(min=1000000000000000, max=9999999999999999))
    }


    # Step 1: Convert the dictionary to a JSON string
    json_data = json.dumps(data_dict)

    # Step 2: URL-encode the JSON string
    url_encoded_data = urllib.parse.quote(json_data)

    # Step 3: Base64-encode the URL-encoded string
    base64_encoded_data = base64.b64encode(url_encoded_data.encode()).decode()


    # Call the function to send the POST request
    post_request(base64_encoded_data)


def post_request(encoded_data):
    headers = {
        "Host": "lerih3.cc",
        "Cookie": "think_lang=en-us; PHPSESSID=e5b98f7fff3342a73525130bb2d2b10d",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://lerih3.cc/",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://lerih3.cc",
        "Dnt": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "Te": "trailers",
    }

    # Send the POST request with the headers and data
    payload = f"data={encoded_data}"
    try:
        response = requests.post(URL, headers=headers, data=payload)
        response=json.loads(response.text)
        print(f"Response Code : {response['code']},Response Message : {response['msg']}")
        if response['code'] == 1:
            I=+1
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def main():
    generate_data()



if __name__ == "__main__":
    # loop infite
    while True:
        main()
        print(f"Account Count : {i}")

