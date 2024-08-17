import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Print all column names for debugging
    print("DataFrame columns:", df.columns)
    
    # Ensure 'icu_hrr.start_bpm' column exists
    if 'icu_hrr.start_bpm' not in df.columns:
        print("Column 'icu_hrr.start_bpm' not found in DataFrame")
        return

    # Generate the plot
    plt.figure()
    plt.plot(df['start_date_local'], df['icu_hrr.start_bpm'], label='Heart Rate', color='red')
    plt.title('Heart Rate Over Time')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate (bpm)')
    plt.legend()

    # Adjust x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    plt.gcf().autofmt_xdate()  # Automatically format x-axis dates

    # Save the plot
    plot_path = os.path.join(output_dir, 'hr_vs_time.png')
    plt.savefig(plot_path, bbox_inches='tight')
    print(f"Heart Rate vs Time plot saved to {plot_path}")

if __name__ == "__main__":
    # Example DataFrame for testing
    import pandas as pd
    data = {
        'start_date_local': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'icu_hrr.start_bpm': range(60, 70)
    }
    df = pd.DataFrame(data)
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    output_dir = "output"
    generate_plot(df, output_dir)
