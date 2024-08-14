# main.py

from config.settings import API_BASE_URL, OLDEST_DATE, NEWEST_DATE, PORT, OUTPUT_DIR
from scripts.fetch_data import fetch_running_data
from scripts.process_data import process_data
from scripts.generate_plot import generate_plot
from scripts.generate_report import generate_html_report
from scripts.http_server import start_http_server
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    athlete_id = os.getenv("ATHLETE_ID")
    
    raw_data = fetch_running_data(API_BASE_URL, athlete_id, api_key, OLDEST_DATE, NEWEST_DATE)
    df = process_data(raw_data)
    
    image_path = generate_plot(df, OUTPUT_DIR)
    generate_html_report(image_path, OUTPUT_DIR)
    
    start_http_server(OUTPUT_DIR, PORT)

if __name__ == "__main__":
    main()
