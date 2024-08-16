import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Print all column names for debugging
    print("DataFrame columns:", df.columns)
    
    # Ensure 'distance_km' column exists
    if 'distance_km' not in df.columns:
        print("Column 'distance_km' not found in DataFrame")
        return

    # Generate the plot
    plt.figure()
    plt.plot(df['start_date_local'], df['distance_km'], label='Distance (km)', color='blue')
    plt.title('Distance Over Time')
    plt.xlabel('Time')
    plt.ylabel('Distance (km)')
    plt.legend()




    plt.xticks(rotation=45, ha='right')
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    plot_path = os.path.join(output_dir, 'distance_over_time.png')
    plt.savefig(plot_path)
    print(f"Distance Over Time plot saved to {plot_path}")

if __name__ == "__main__":
    # Example DataFrame for testing
    import pandas as pd
    data = {
        'start_date_local': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'distance_km': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    df = pd.DataFrame(data)
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    output_dir = "output"
    generate_plot(df, output_dir)
