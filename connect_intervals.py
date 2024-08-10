import os
import subprocess
import requests
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from config import API_BASE_URL
import http.server
import socketserver
from threading import Thread

# Non-changing values
TIMEOUT = 10  # Timeout in seconds for API requests
OLDEST_DATE = "1970-01-01"  # Start date set far in the past to include all activities
NEWEST_DATE = "2025-01-01"  # A date in the future to include all activities

# Load sensitive data from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
ATHLETE_ID = os.getenv("ATHLETE_ID")

# Endpoint for retrieving activities with the required parameters
endpoint = f"athlete/{ATHLETE_ID}/activities?oldest={OLDEST_DATE}&newest={NEWEST_DATE}"

# Function to start the HTTP server
def start_server(directory, port=8080):
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    print(f"Serving at port {port}")
    httpd.serve_forever()

# Automatically generate and serve the HTML file
def generate_and_serve():
    output_dir = os.path.abspath(os.path.dirname(__file__))

    # Make the request with Basic Authentication
    response = requests.get(f"{API_BASE_URL}{endpoint}", auth=("API_KEY", API_KEY), timeout=TIMEOUT)

    # Check if the request was successful
    if response.status_code == 200:
        activities = response.json()
        
        # Filter for running activities
        running_activities = [activity for activity in activities if activity.get('type') == 'Run']
        
        if running_activities:
            # Convert running activities to a DataFrame
            df = pd.json_normalize(running_activities)
            
            # Convert date columns to datetime
            df['start_date_local'] = pd.to_datetime(df['start_date_local'])
            
            # Generate Pace and Heart Rate vs. Time graph
            if 'average_speed' in df.columns and 'average_heartrate' in df.columns:
                df['pace'] = 1 / df['average_speed']  # Assuming speed is in m/s, convert to min/km
                
                fig, ax1 = plt.subplots()

                ax1.set_xlabel('Date')
                ax1.set_ylabel('Pace (min/km)', color='tab:blue')
                ax1.plot(df['start_date_local'], df['pace'], color='tab:blue', label='Pace')
                ax1.tick_params(axis='y', labelcolor='tab:blue')

                ax2 = ax1.twinx()  # Instantiate a second axes that shares the same x-axis
                ax2.set_ylabel('Heart Rate (bpm)', color='tab:red')
                ax2.plot(df['start_date_local'], df['average_heartrate'], color='tab:red', label='Heart Rate')
                ax2.tick_params(axis='y', labelcolor='tab:red')

                fig.tight_layout()  # To prevent the labels from overlapping
                plt.title('Pace and Heart Rate vs. Time')

                # Save the plot to a PNG file in the same directory as the HTML
                graph_filename = os.path.join(output_dir, 'pace_heartrate_vs_time.png')
                plt.savefig(graph_filename)
                
                # Generate HTML file with a relative path to the graph
                html_content = f"""
                <html>
                <head><title>Pace and Heart Rate Graph</title></head>
                <body>
                <h1>Pace and Heart Rate vs. Time</h1>
                <img src="{os.path.basename(graph_filename)}" alt="Pace and Heart Rate Graph">
                </body>
                </html>
                """
                
                html_filename = os.path.join(output_dir, 'pace_heartrate_vs_time.html')
                with open(html_filename, 'w') as file:
                    file.write(html_content)
                
                # Start the HTTP server in a separate thread
                server_thread = Thread(target=start_server, args=(output_dir,))
                server_thread.daemon = True
                server_thread.start()

                # Keep the script running
                print("HTTP server is running. Access the report at http://localhost:8080/pace_heartrate_vs_time.html")
                input("Press Enter to stop the server...\n")

        else:
            print(json.dumps({"message": "No running activities found."}, indent=4))
    else:
        print(f"Failed to retrieve activities: {response.status_code}")
        print("Error:", response.text)

if __name__ == "__main__":
    generate_and_serve()
