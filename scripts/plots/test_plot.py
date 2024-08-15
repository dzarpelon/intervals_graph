import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    plt.figure()
    plt.plot(df['start_date_local'], df['distance'], label='Distance')
    plt.xlabel('Date')
    plt.ylabel('Distance (km)')
    plt.title('Test Plot: Distance Over Time')
    plt.legend()
    plt_path = os.path.join(output_dir, 'plots', 'test_plot.png')
    plt.savefig(plt_path)
    print(f"Test plot saved to {plt_path}")
