import requests
from dotenv import load_dotenv
import os
from config import API_BASE_URL, ENDPOINT_PROFILE

# Non-changing values
TIMEOUT = 10  # Timeout in seconds for API requests

# Load sensitive data from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
ATHLETE_ID = os.getenv("ATHLETE_ID")

# Construct the correct endpoint using the athlete ID
endpoint = ENDPOINT_PROFILE.replace("{id}", ATHLETE_ID)

# Make the request with Basic Authentication
response = requests.get(f"{API_BASE_URL}{endpoint}", auth=("API_KEY", API_KEY), timeout=TIMEOUT)

# Check if the request was successful
if response.status_code == 200:
    print("Connected successfully!")
    print("Response Data:", response.json())
else:
    print(f"Failed to connect: {response.status_code}")
    print("Error:", response.text)
