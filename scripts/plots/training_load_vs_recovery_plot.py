import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Print all column names for debugging
    print("DataFrame columns:", df.columns)
    
    # Assuming 'icu_pm_ftp' as 'training_load' and 'icu_hrr.hrr' as 'recovery_time' for this example
    if 'icu_pm_ftp' not in df.columns or 'icu_hrr.hrr' not in df.columns:
        print("Column 'icu_pm_ftp' or 'icu_hrr.hrr' not found in DataFrame")
        return

    # Generate the plot
    plt.figure()
    plt.plot(df['start_date_local'], df['icu_pm_ftp'], label='Training Load', color='blue')
    plt.plot(df['start_date_local'], df['icu_hrr.hrr'], label='Recovery Time', color='red')
    plt.title('Training Load vs Recovery Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()




    plt.xticks(rotation=45, ha='right')
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    plot_path = os.path.join(output_dir, 'training_load_vs_recovery.png')
    plt.savefig(plot_path)
    print(f"Training Load vs Recovery plot saved to {plot_path}")

if __name__ == "__main__":
    # Example DataFrame for testing
    import pandas as pd
    data = {
        'start_date_local': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'icu_pm_ftp': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],  # Mock data for training load
        'icu_hrr.hrr': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]   # Mock data for recovery time
    }
    df = pd.DataFrame(data)
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    output_dir = "output"
    generate_plot(df, output_dir)
