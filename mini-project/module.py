import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_coral_d18O(core_depth=100, temp_trend=-0.02, baseline_d18o=-5, location="Fake Coral Location", filename="simulated_d18o_dataset.csv"):
    """
    Generate a synthetic coral δ¹⁸O dataset with depth in mm.

    Parameters:
        core_depth (int): Total depth of the coral core in mm.
        temp_trend (float): The isotope warming trend (default -0.02 per mm).
        baseline_d18o (float): The baseline δ¹⁸O value.
        location (str): Name of the location for labeling.
        filename (str): Name of the file to save the dataset.

    Returns:
        df_d18o (DataFrame): DataFrame with Depth (mm) and δ¹⁸O values.
    """
    np.random.seed(42)  # Ensures reproducibility
    core_depth_values = np.arange(0, core_depth + 1, 1)  # Depth values from 0 to core_depth mm
    seasonal_cycle = np.sin(2 * np.pi * core_depth_values / 12)  # Simulated seasonal cycle
    noise = np.random.normal(0, 0.1, size=len(core_depth_values))  # Small noise

    # Apply the temperature trend to δ¹⁸O
    temp_effect = temp_trend * core_depth_values  # Decreasing temperature increases δ¹⁸O
    d18o_values = baseline_d18o + temp_effect + seasonal_cycle + noise  # Generate synthetic δ¹⁸O values

    # Create a dataframe
    df_d18o = pd.DataFrame({"Depth (mm)": core_depth_values, "δ18O (‰)": d18o_values})

    # Save to CSV
    df_d18o.to_csv(filename, index=False)

    # Plot the data
    plt.figure(figsize=(8, 5))
    plt.style.use('classic')
    plt.plot(core_depth_values, d18o_values, marker='o', linestyle='-', color='black', label='Simulated δ18O')
    plt.xlabel('Depth (mm)')
    plt.ylabel('δ18O (‰)')
    plt.title(f"Simulated δ¹⁸O Data - {location}")    
    plt.gca().invert_xaxis()  # Depth increases downward in time
    plt.grid()
    plt.legend()
    plt.show()

    return df_d18o