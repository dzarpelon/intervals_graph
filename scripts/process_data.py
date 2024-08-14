# scripts/process_data.py

import pandas as pd

def process_data(raw_data):
    # Filter for running activities
    running_activities = [activity for activity in raw_data if activity.get('type') == 'Run']
    
    if not running_activities:
        print("No running activities found.")
        return None
    
    # Convert to DataFrame
    df = pd.json_normalize(running_activities)
    
    # Convert date columns to datetime
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    
    # Calculate Pace from average_speed
    if 'average_speed' in df.columns:
        df['Pace'] = 1 / df['average_speed'] * 1000 / 60  # Convert speed (m/s) to pace (min/km)
    
    return df
