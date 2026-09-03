'''
import math
import matplotlib.pyplot as plt
import numpy as np


def calculate_exact_phi():
    """Calculates the exact mathematical value of the Golden Ratio."""
    return (1 + math.sqrt(5)) / 2


def approximate_phi_via_fibonacci(iterations=40):
    """Approximates the Golden Ratio using consecutive Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(iterations):
        a, b = b, a + b
    return b / a


def plot_golden_spiral(phi):
    """Generates and displays a visual plot of the Golden Spiral."""
    # Create theta values (angles for the spiral over multiple rotations)
    theta = np.linspace(0, 5 * np.pi, 1000)

    # Calculate radius using the Golden Ratio growth factor
    # Growth factor b represents a scale change every 90 degrees (pi/2)
    b_factor = np.log(phi) / (np.pi / 2)
    r = 0.1 * np.exp(b_factor * theta)

    # Convert polar coordinates (r, theta) to Cartesian coordinates (x, y)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Set up the matplotlib figure
    plt.figure(figsize=(8, 8), facecolor="#f7f7f7")
    plt.plot(x, y, color="#D4AF37", linewidth=2.5, label="Golden Spiral (φ)")

    # Style the visual graph
    plt.title("The Golden Ratio (Golden Spiral)", fontsize=16, fontweight="bold")
    plt.xlabel("X Axis", fontsize=12)
    plt.ylabel("Y Axis", fontsize=12)
    plt.axhline(0, color="gray", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="gray", linewidth=0.5, linestyle="--")
    plt.axis("equal")  # Ensures the spiral isn't distorted
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper left", fontsize=12)

    print("\nDisplaying the Golden Spiral plot window...")
    plt.show()


if __name__ == "__main__":
    print("=== GOLDEN RATIO GENERATOR ===")

    # 1. Calculate direct value
    exact_phi = calculate_exact_phi()
    print(f"Exact Mathematical Value (φ): {exact_phi}")

    # 2. Calculate approximation value
    fib_phi = approximate_phi_via_fibonacci()
    print(f"Fibonacci Approximation (φ):  {fib_phi}")
    print(f"Calculation Difference:       {abs(exact_phi - fib_phi)}")

    # 3. Trigger visual plot
    plot_golden_spiral(exact_phi)
'''

import math
import matplotlib.pyplot as plt
import numpy as np

# 1. Define Constants
NUM_STARS = 15000  # Total stars to generate
PHI = (1 + np.sqrt(5)) / 2  # The Golden Ratio
GOLDEN_B = np.log(PHI) / (np.pi / 2)  # Tightness factor based on Golden Ratio


def generate_golden_galaxy():
    """Generates stars distributed according to Golden Ratio spiral arms."""
    x_stars = []
    y_stars = []
    colors = []

    # Number of main spiral arms
    num_arms = 2

    for i in range(NUM_STARS):
        # Assign a star to one of the arms
        arm_offset = (i % num_arms) * np.pi

        # Distribution: more stars near the center, fewer at edges
        t = np.random.uniform(0, 1) ** 1.5 * (4 * np.pi)

        # Logarithmic spiral equation using the Golden Ratio growth factor
        r = 0.2 * np.exp(GOLDEN_B * t)

        # Base spiral coordinates
        x_base = r * np.cos(t + arm_offset)
        y_base = r * np.sin(t + arm_offset)

        # Add Gaussian noise (scatter) so it looks like natural stardust
        scatter_spread = 0.15 * (r**0.7)
        x_noise = np.random.normal(0, scatter_spread)
        y_noise = np.random.normal(0, scatter_spread)

        x_stars.append(x_base + x_noise)
        y_stars.append(y_base + y_noise)

        # Determine color based on distance from core (Hot Core vs Cool Arms)
        if r < 0.8:
            colors.append("#FFFFFF")  # Brilliant White Core
        elif r < 2.5:
            colors.append("#ADD8E6")  # Vibrant Blue/Cyan Stars
        else:
            colors.append("#D4AF37")  # Golden-yellow Outer Stars

    return np.array(x_stars), np.array(y_stars), colors


def plot_galaxy(x, y, colors):
    """Plots the generated stars onto a cinematic space-themed canvas."""
    fig, ax = plt.subplots(figsize=(9, 9), facecolor="#03030c")
    ax.set_facecolor("#03030c")

    # Draw a faint theoretical golden spiral overlay for reference
    theta_line = np.linspace(0, 4.5 * np.pi, 1000)
    for offset in [0, np.pi]:
        r_line = 0.2 * np.exp(GOLDEN_B * theta_line)
        xl = r_line * np.cos(theta_line + offset)
        yl = r_line * np.sin(theta_line + offset)
        ax.plot(
            xl,
            yl,
            color="#FFD700",
            linestyle="--",
            linewidth=1.2,
            alpha=0.3,
            label="Golden Ratio Path" if offset == 0 else "",
        )

    # Scatter plot the stars with variable sizes
    sizes = np.random.uniform(0.5, 4.0, size=NUM_STARS)
    ax.scatter(x, y, c=colors, s=sizes, alpha=0.7, edgecolors="none")

    # CORRECTED CORE GLOW: Passing proper coordinates and removing 'blur'
    ax.scatter([0], [0], color="#FFFFFF", s=1200, alpha=0.2, zorder=0)
    ax.scatter([0], [0], color="#ADD8E6", s=3000, alpha=0.08, zorder=0)

    # UI and styling adjustments
    ax.set_title(
        "Hypothetical 'Golden Ratio' Spiral Galaxy Simulation",
        color="white",
        fontsize=14,
        fontweight="bold",
        pad=15,
    )
    ax.axis("equal")
    ax.axis("off")  # Hides graph axes to make it look like space
    ax.legend(loc="lower right", facecolor="#03030c", edgecolor="none", labelcolor="w")

    plt.show()


if __name__ == "__main__":
    print("Generating 15,000 cosmic stars aligned to Golden Ratio (\u03a6)...")
    x, y, colors = generate_golden_galaxy()
    plot_galaxy(x, y, colors)

