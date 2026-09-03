import matplotlib.pyplot as plt
import numpy as np

def simulate_sunflower(num_seeds=800):
    """
    Simulates seed packing using the Golden Angle.
    """
    # 1. Define the Golden Angle in radians (~2.3999 radians or 137.5 degrees)
    golden_ratio = (1 + 5 ** 0.5) / 2
    golden_angle = 2 * np.pi * (1 - 1 / golden_ratio)
    
    # 2. Generate indices for each seed
    indices = np.arange(1, num_seeds + 1)
    
    # 3. Calculate distance (r) and angle (theta) for each seed
    # Distance increases with the square root of the index to spread seeds evenly
    r = np.sqrt(indices)
    theta = indices * golden_angle
    
    # 4. Convert Polar coordinates to Cartesian coordinates (X, Y)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # 5. Plot the simulation
    plt.figure(figsize=(8, 8), facecolor='black')
    
    # Color the seeds from inside out to visually reveal the spiraling arms
    plt.scatter(x, y, c=indices, cmap='YlOrBr', edgecolors='none', s=25)
    
    # Clean up the chart presentation
    plt.axis('off')
    plt.axis('equal')
    plt.title(f"Nature's Packing Efficiency\n({num_seeds} Seeds using {137.5}° Angle)", 
              color='white', fontsize=14, fontweight='bold')
    
    plt.show()

# Run the simulation
simulate_sunflower(800)
