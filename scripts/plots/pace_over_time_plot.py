# scripts/plots/pace_over_time_plot.py
import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    plt.figure()
    plt.plot(df['start_date_local'], df['Pace'], label='Pace', color='blue')
    plt.title('Pace Over Time')
    plt.xlabel('Date')
    plt.ylabel('Pace')
    plt.legend()




    plt.xticks(rotation=45, ha='right')
    plt.xticks(rotation=45, ha="right")

    plot_path = os.path.join(output_dir, 'pace_over_time.png')
    plt.savefig(plot_path)
    print(f"Pace Over Time plot saved to {plot_path}")

# For manual testing
if __name__ == "__main__":
    import pandas as pd
    data = {
        'start_date_local': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'Pace': range(6, 16)
    }
    df = pd.DataFrame(data)
    output_dir = "output"
    generate_plot(df, output_dir)
