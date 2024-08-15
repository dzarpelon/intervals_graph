import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    plt.figure()
    plt.plot(df['start_date_local'], df['average_speed'], label='Average Speed')
    plt.xlabel('Date')
    plt.ylabel('Speed (km/h)')
    plt.title('New Test Plot: Average Speed Over Time')
    plt.legend()
    plt_path = os.path.join(output_dir, 'plots', 'new_test_plot.png')
    plt.savefig(plt_path)
    print(f"New test plot saved to {plt_path}")
