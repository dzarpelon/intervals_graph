import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Ensure 'distance_km' column exists
    if 'distance_km' not in df.columns:
        if 'distance' in df.columns:
            # Assuming distance is in meters and converting to kilometers
            df['distance_km'] = df['distance'] / 1000
        else:
            print("Column 'distance_km' or 'distance' not found in DataFrame")
            return

    # Group by week and sum the distances
    df['week'] = df['start_date_local'].dt.isocalendar().week
    weekly_mileage = df.groupby('week')['distance_km'].sum()

    # Generate the plot
    plt.figure()
    plt.plot(weekly_mileage.index, weekly_mileage.values, label='Weekly Mileage', color='blue', marker='o')
    plt.title('Weekly Mileage')
    plt.xlabel('Week')
    plt.ylabel('Mileage (km)')
    plt.legend()




    plt.xticks(rotation=45, ha='right')
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    plot_path = os.path.join(output_dir, 'weekly_mileage.png')
    plt.savefig(plot_path)
    print(f"Weekly Mileage plot saved to {plot_path}")

if __name__ == "__main__":
    import pandas as pd
    data = {
        'start_date_local': pd.date_range(start='2024-01-01', periods=100, freq='D'),
        'distance': range(1000, 11000, 100)
    }
    df = pd.DataFrame(data)
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    output_dir = "output"
    generate_plot(df, output_dir)
