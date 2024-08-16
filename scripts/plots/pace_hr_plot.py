# scripts/plots/pace_hr_plot.py
import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    plt.figure()
    plt.plot(df['start_date_local'], df['Pace'], label='Pace')
    plt.plot(df['start_date_local'], df['average_heartrate'], label='Heart Rate', color='red')
    plt.title('Pace and Heart Rate Over Time')
    plt.xlabel('Time')
    plt.ylabel('Pace / Heart Rate')
    plt.legend()

    # Ensure the plots directory exists
    plots_dir = os.path.join(output_dir, 'plots')
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)

    # Save the plot
    plot_path = os.path.join(plots_dir, 'pace_hr_plot.png')
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")
