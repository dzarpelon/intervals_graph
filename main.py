# main.py

from config.settings import API_BASE_URL, OLDEST_DATE, NEWEST_DATE, PORT
from scripts.fetch_data import fetch_running_data
from scripts.process_data import process_data
from scripts.plot_manager import generate_main_html_report, load_and_run_plot_script, generate_all_plots
from scripts.http_server import start_http_server
import os
from dotenv import load_dotenv
from watchdog.observers import Observer
from scripts.plot_event_handler import PlotFileEventHandler

# Hardcoded paths
PLOT_SCRIPTS_DIR = os.path.join(os.getcwd(), 'scripts', 'plots')
OUTPUT_PLOTS_DIR = os.path.join(os.getcwd(), 'output', 'plots')

# Set the working directory to the project root
os.chdir('/workspaces/python/intervals_graph')

def start_file_observer(df):
    """Start the watchdog observer to monitor plot scripts."""
    event_handler = PlotFileEventHandler(df, OUTPUT_PLOTS_DIR)
    observer = Observer()
    observer.schedule(event_handler, path=PLOT_SCRIPTS_DIR, recursive=False)
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
    generate_all_plots(df, OUTPUT_PLOTS_DIR)
    generate_main_html_report(OUTPUT_PLOTS_DIR)
    
    # Start monitoring the plot scripts for changes
    observer = start_file_observer(df)
    
    # Start the HTTP server
    try:
        start_http_server(OUTPUT_PLOTS_DIR, PORT)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
