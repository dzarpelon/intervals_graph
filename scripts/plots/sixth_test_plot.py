import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    plt.figure()
    plt.plot(df['start_date_local'], df['average_cadence'], label='Average Cadence')
    plt.xlabel('Date')
    plt.ylabel('Cadence (rpm)')
    plt.title('Sixth Test Plot: Average Cadence Over Time')
    plt.legend()
    plt_path = os.path.join(output_dir, 'plots', 'sixth_test_plot.png')
    plt.savefig(plt_path)
    print(f"Sixth test plot saved to {plt_path}")