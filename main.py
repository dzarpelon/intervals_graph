# main.py
from config.settings import API_BASE_URL, OLDEST_DATE, NEWEST_DATE, PORT, OUTPUT_DIR
from scripts.fetch_data import fetch_running_data
from scripts.process_data import process_data
from scripts.plot_manager import generate_main_html_report, load_and_run_plot_script, generate_all_plots
from scripts.http_server import start_http_server
import os
from dotenv import load_dotenv
from watchdog.observers import Observer
from scripts.plot_event_handler import PlotFileEventHandler

# Set the working directory to the project root
os.chdir('/workspaces/python/intervals_graph')

def start_file_observer(df, output_dir):
    """Start the watchdog observer to monitor plot scripts."""
    event_handler = PlotFileEventHandler(df, output_dir)
    observer = Observer()
    observer.schedule(event_handler, path="scripts/plots", recursive=False)
    observer.start()
    return observer

def main():
    load_dotenv()  # Load environment variables from .env
    api_key = os.getenv("API_KEY")
    athlete_id = os.getenv("ATHLETE_ID")
    
    # Fetch and process data
    raw_data = fetch_running_data(API_BASE_URL, athlete_id, api_key, OLDEST_DATE, NEWEST_DATE)
    df = process_data(raw_data)
    
    # Generate initial plots and HTML report
    generate_all_plots(df, OUTPUT_DIR)
    generate_main_html_report(OUTPUT_DIR)
    
    # Start monitoring the plot scripts for changes
    observer = start_file_observer(df, OUTPUT_DIR)
    
    # Start the HTTP server
    try:
        start_http_server(OUTPUT_DIR, PORT)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
