import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    print("Starting to generate ninth plot")
    
    # Check if the DataFrame contains the expected columns
    print(f"DataFrame columns: {df.columns}")
    
    if 'start_date_local' not in df.columns or 'average_speed' not in df.columns:
        print("Required columns not found in the DataFrame.")
        return
    
    print("Columns are present. Proceeding to plot.")
    
    plt.figure()
    plt.plot(df['start_date_local'], df['average_speed'], label='Average Speed')
    plt.xlabel('Date')
    plt.ylabel('Speed (m/s)')
    plt.title('Ninth Test Plot: Average Speed Over Time')
    plt.legend()
    plt_path = os.path.join(output_dir, 'plots', 'ninth_test_plot.png')
    plt.savefig(plt_path)
    print(f"Ninth test plot saved to {plt_path}")
