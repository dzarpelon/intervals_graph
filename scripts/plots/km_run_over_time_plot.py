# scripts/plots/km_run_over_time_plot.py
import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Debugging: Print DataFrame columns
    print("DataFrame columns:", df.columns)

    # Check if 'distance' column is present and convert it to 'distance_km'
    if 'distance' in df.columns:
        df['distance_km'] = df['distance'] / 1000  # Convert meters to kilometers
    else:
        print("Required column 'distance' is missing in the DataFrame.")
        return

    # Check if the necessary columns are present
    if 'start_date_local' not in df.columns or 'distance_km' not in df.columns:
        print("Required columns are missing in the DataFrame.")
        return
    
    # Generate the plot
    plt.figure()
    plt.plot(df['start_date_local'], df['distance_km'], label='Distance (km)', color='blue')
    plt.title('Distance Run Over Time')
    plt.xlabel('Time')
    plt.ylabel('Distance (km)')
    plt.legend()

    # Ensure the plots directory exists
    plots_dir = os.path.join(output_dir, 'plots')
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)

    # Save the plot
    plot_path = os.path.join(plots_dir, 'km_run_over_time.png')
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")
