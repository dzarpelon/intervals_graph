# scripts/fetch_data.py

import requests

def fetch_running_data(api_base_url, athlete_id, api_key, oldest_date, newest_date):
    endpoint = f"athlete/{athlete_id}/activities?oldest={oldest_date}&newest={newest_date}"
    response = requests.get(f"{api_base_url}{endpoint}", auth=("API_KEY", api_key))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve activities: {response.status_code}")
        print("Error:", response.text)
        return None
