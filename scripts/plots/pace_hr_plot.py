# scripts/plots/pace_hr_plot.py

import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Check if the dataframe is empty or None
    if df is None or df.empty:
        print("No data to plot.")
        return None

    # Generate the Pace and Heart Rate vs. Time plot
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Time')
    ax1.set_ylabel('Pace (min/km)', color='tab:blue')
    ax1.plot(df['start_date_local'], df['Pace'], color='tab:blue', label='Pace')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Heart Rate (bpm)', color='tab:red')
    ax2.plot(df['start_date_local'], df['average_heartrate'], color='tab:red', label='Heart Rate')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
    fig.tight_layout()
    plt.title('Pace and Heart Rate vs. Time')

    # Save the plot as a PNG file in the specified output directory
    plot_path = os.path.join(output_dir, 'plots', 'pace_hr_plot.png')
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")
