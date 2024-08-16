import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Print all column names for debugging
    print("DataFrame columns:", df.columns)
    
    # Assuming 'icu_hrr.start_bpm' as the heart rate column and 'Pace' as the pace column
    if 'icu_hrr.start_bpm' not in df.columns or 'Pace' not in df.columns:
        print("Column 'icu_hrr.start_bpm' or 'Pace' not found in DataFrame")
        return

    # Generate the plot
    plt.figure()
    plt.scatter(df['Pace'], df['icu_hrr.start_bpm'], label='HR vs Pace', color='purple')
    plt.title('Heart Rate vs Pace')
    plt.xlabel('Pace')
    plt.ylabel('Heart Rate (bpm)')
    plt.legend()




    plt.xticks(rotation=45, ha='right')
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    plot_path = os.path.join(output_dir, 'hr_vs_pace_plot.png')
    plt.savefig(plot_path)
    print(f"HR vs Pace plot saved to {plot_path}")

if __name__ == "__main__":
    # Example DataFrame for testing
    import pandas as pd
    data = {
        'Pace': range(10),  # Mock data for pace
        'icu_hrr.start_bpm': [150, 155, 152, 158, 160, 162, 165, 168, 170, 172]  # Mock data for heart rate
    }
    df = pd.DataFrame(data)
    output_dir = "output"
    generate_plot(df, output_dir)
