import matplotlib.pyplot as plt
import numpy as np

# 1. Define Constants
NUM_STARS = 18000  # Total stars to generate
PHI = (1 + np.sqrt(5)) / 2  # The Golden Ratio
GOLDEN_B = np.log(PHI) / (np.pi / 2)  # Tightness factor based on Golden Ratio


def generate_golden_galaxy_3d():
    """Generates stars distributed in 3D according to Golden Ratio spiral arms."""
    x_stars = []
    y_stars = []
    z_stars = []
    colors = []

    num_arms = 2

    for i in range(NUM_STARS):
        arm_offset = (i % num_arms) * np.pi

        # Radial distribution: cluster tightly toward the core
        t = np.random.uniform(0, 1) ** 1.6 * (4.5 * np.pi)
        r = 0.2 * np.exp(GOLDEN_B * t)

        # Base 2D spiral path
        x_base = r * np.cos(t + arm_offset)
        y_base = r * np.sin(t + arm_offset)

        # 2D horizontal scattering (gas cloud spread)
        scatter_spread = 0.18 * (r**0.7)
        x_noise = np.random.normal(0, scatter_spread)
        y_noise = np.random.normal(0, scatter_spread)

        # 3D vertical scattering (height thickness)
        # Galaxies bulge significantly at the core (small r) and flatten at the rim (large r)
        height_bulge = 0.4 * np.exp(-0.7 * r) + 0.05
        z_noise = np.random.normal(0, height_bulge)

        x_stars.append(x_base + x_noise)
        y_stars.append(y_base + y_noise)
        z_stars.append(z_noise)

        # Dynamic deep space color grading based on radius
        if r < 0.7:
            colors.append("#FFFFFF")  # Brilliant white core
        elif r < 2.0:
            colors.append("#87CEEB")  # Sky blue inner arms
        elif r < 4.0:
            colors.append("#4169E1")  # Royal blue outer arms
        else:
            colors.append("#D4AF37")  # Golden perimeter stars

    return np.array(x_stars), np.array(y_stars), np.array(z_stars), colors


def plot_galaxy_3d(x, y, z, colors):
    """Plots the stars in a fully interactive, rotatable 3D space canvas."""
    fig = plt.figure(figsize=(10, 10), facecolor="#03030c")

    # Initialize 3D axis projection
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#03030c")

    # Render stars with size variation based on randomized depth perspective
    sizes = np.random.uniform(0.3, 3.5, size=NUM_STARS)
    ax.scatter(x, y, z, c=colors, s=sizes, alpha=0.6, edgecolors="none")

    # FIXED: Proper center positioning arrays for X, Y, Z coordinates
    ax.scatter([0], [0], [0], color="#FFFFFF", s=2500, alpha=0.15, edgecolors="none")
    ax.scatter([0], [0], [0], color="#87CEEB", s=5000, alpha=0.06, edgecolors="none")

    # UI adjustments and removing axes lines to mimic dark space
    ax.set_title(
        "Interactive 3D 'Golden Ratio' Galaxy Simulation\n(Click & drag to rotate and spin)",
        color="white",
        fontsize=14,
        fontweight="bold",
        pad=10,
    )

    # Set proportional viewing bounds
    max_range = np.array([x.max() - x.min(), y.max() - y.min(), 5.0]).max() / 2.0
    mid_x = (x.max() + x.min()) * 0.5
    mid_y = (y.max() + y.min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(-max_range / 3, max_range / 3)

    # Hide grids, numbers, and glass panes for an immersive look
    ax.grid(False)
    ax.axis("off")

    print("\nLaunching 3D Canvas...")
    print("-> Left-click and drag to rotate the galaxy horizontally or vertically.")
    print("-> Right-click and drag (or use scroll wheel) to zoom in and out.")
    plt.show()


if __name__ == "__main__":
    print("Generating 18,000 cosmic coordinates mapped to a 3D Golden Spiral...")
    x, y, z, colors = generate_golden_galaxy_3d()
    plot_galaxy_3d(x, y, z, colors)
