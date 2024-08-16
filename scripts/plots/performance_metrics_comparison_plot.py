import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Print all column names for debugging
    print("DataFrame columns:", df.columns)
    
    # Assuming 'icu_pm_cp' as 'metric_1' and 'icu_pm_w_prime' as 'metric_2'
    if 'icu_pm_cp' not in df.columns or 'icu_pm_w_prime' not in df.columns:
        print("Column 'icu_pm_cp' or 'icu_pm_w_prime' not found in DataFrame")
        return

    # Generate the plot
    plt.figure()
    plt.plot(df['start_date_local'], df['icu_pm_cp'], label='Metric 1: CP', color='blue')
    plt.plot(df['start_date_local'], df['icu_pm_w_prime'], label='Metric 2: W\'', color='green')
    plt.title('Performance Metrics Comparison Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()




    plt.xticks(rotation=45, ha='right')
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    plot_path = os.path.join(output_dir, 'performance_metrics_comparison.png')
    plt.savefig(plot_path)
    print(f"Performance Metrics Comparison plot saved to {plot_path}")

if __name__ == "__main__":
    # Example DataFrame for testing
    import pandas as pd
    data = {
        'start_date_local': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'icu_pm_cp': [300, 320, 310, 330, 340, 335, 345, 350, 360, 370],  # Mock data for metric 1
        'icu_pm_w_prime': [12000, 12500, 12300, 12700, 13000, 12800, 13200, 13500, 13700, 14000]  # Mock data for metric 2
    }
    df = pd.DataFrame(data)
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    output_dir = "output"
    generate_plot(df, output_dir)
