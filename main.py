import requests
from dotenv import load_dotenv
import os
from config import API_BASE_URL, ENDPOINT

# Non-changing values
TIMEOUT = 10  # Timeout in seconds for API requests

# Load sensitive data from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# API request
response = requests.get(f"{API_BASE_URL}{ENDPOINT}", auth=(API_KEY, ''), timeout=TIMEOUT)

# Check if the request was successful
if response.status_code == 200:
    print("Connected successfully!")
    print("Response Data:", response.json())
else:
    print(f"Failed to connect: {response.status_code}")
    print("Error:", response.text)
