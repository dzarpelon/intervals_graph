import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    print("Starting to generate plot")
    
    # Check if the DataFrame contains the expected columns
    print(f"DataFrame columns: {df.columns}")
    
    if 'start_date_local' not in df.columns or 'total_elevation_gain' not in df.columns:
        print("Required columns not found in the DataFrame.")
        return
    
    print("Columns are present. Proceeding to plot.")
    
    plt.figure()
    plt.plot(df['start_date_local'], df['total_elevation_gain'], label='Total Elevation Gain')
    plt.xlabel('Date')
    plt.ylabel('Elevation Gain (m)')
    plt.title('Seventh Test Plot: Total Elevation Gain Over Time')
    plt.legend()
    plt_path = os.path.join(output_dir, 'plots', 'seventh_test_plot.png')
    plt.savefig(plt_path)
    print(f"Seventh test plot saved to {plt_path}")
