import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Print all column names for debugging
    print("DataFrame columns:", df.columns)
    
    # Assuming 'total_elevation_gain' is the correct column for elevation gain
    if 'total_elevation_gain' not in df.columns or 'start_date_local' not in df.columns:
        print("Column 'total_elevation_gain' or 'start_date_local' not found in DataFrame")
        return

    # Generate the plot
    plt.figure()
    plt.plot(df['start_date_local'], df['total_elevation_gain'], label='Elevation Gain', color='orange')
    plt.title('Elevation Gain Over Time')
    plt.xlabel('Time')
    plt.ylabel('Elevation Gain (m)')
    plt.legend()




    plt.xticks(rotation=45, ha='right')
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    plot_path = os.path.join(output_dir, 'elevation_gain_over_time.png')
    plt.savefig(plot_path)
    print(f"Elevation Gain Over Time plot saved to {plot_path}")

if __name__ == "__main__":
    # Example DataFrame for testing
    import pandas as pd
    data = {
        'start_date_local': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'total_elevation_gain': [50, 75, 100, 120, 140, 160, 180, 200, 220, 240]  # Mock data for elevation gain
    }
    df = pd.DataFrame(data)
    output_dir = "output"
    generate_plot(df, output_dir)
