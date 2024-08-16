import matplotlib.pyplot as plt
import os

def generate_plot(df, output_dir):
    # Assume a lap is defined as every 'x' meters, here we simulate it based on indices
    lap_length = 1000  # Define lap length in meters, adjust this based on your needs
    df['lap'] = df.index // lap_length
    
    # Group by 'lap' and calculate average pace per lap
    lap_data = df.groupby('lap')['Pace'].mean().reset_index()
    
    # Generate the plot
    plt.figure()
    plt.plot(lap_data['lap'], lap_data['Pace'], marker='o', label='Average Pace per Lap', color='blue')
    plt.title('Lap Analysis')
    plt.xlabel('Lap Number')
    plt.ylabel('Average Pace')
    plt.legend()




    plt.xticks(rotation=45, ha='right')
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    plot_path = os.path.join(output_dir, 'lap_analysis_plot.png')
    plt.savefig(plot_path)
    print(f"Lap analysis plot saved to {plot_path}")

# Simulate the environment for manual testing
if __name__ == "__main__":
    # Example DataFrame for testing
    import pandas as pd
    data = {
        'start_date_local': pd.date_range(start='2024-01-01', periods=5000, freq='T'),
        'Pace': range(5000)
    }
    df = pd.DataFrame(data)
    output_dir = "output"
    generate_plot(df, output_dir)
