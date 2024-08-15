# scripts/plots/km_run_over_time_plot.py

import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Check if the dataframe is empty or None
    if df is None or df.empty:
        print("No data to plot.")
        return None

    # Convert distance to kilometers if it's in meters
    if df['distance'].max() > 100:  # Assuming distance is in meters if max value > 100
        df['distance_km'] = df['distance'] / 1000.0
    else:
        df['distance_km'] = df['distance']

    # Generate the plot: Kilometers run over time
    fig, ax = plt.subplots()

    ax.set_xlabel('Time')
    ax.set_ylabel('Distance (km)')
    ax.plot(df['start_date_local'], df['distance_km'], color='tab:blue', label='Kilometers Run')
    ax.tick_params(axis='y', labelcolor='tab:blue')

    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    fig.tight_layout()
    plt.title('Kilometers Run Over Time')

    # Save the plot as a PNG file in the specified output directory
    plot_path = os.path.join(output_dir, 'plots', 'km_run_over_time.png')
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")
