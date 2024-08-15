import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    print("Starting to generate plot")
    
    # Check if the DataFrame contains the expected columns
    print(f"DataFrame columns: {df.columns}")
    
    if 'start_date_local' not in df.columns or 'average_heartrate' not in df.columns:
        print("Required columns not found in the DataFrame.")
        return
    
    print("Columns are present. Proceeding to plot.")
    
    plt.figure()
    plt.plot(df['start_date_local'], df['average_heartrate'], label='Average Heartrate')
    plt.xlabel('Date')
    plt.ylabel('Heartrate (bpm)')
    plt.title('Eighth Test Plot: Average Heartrate Over Time')
    plt.legend()
    plt_path = os.path.join(output_dir, 'plots', 'eighth_test_plot.png')
    plt.savefig(plt_path)
    print(f"Eighth test plot saved to {plt_path}")
