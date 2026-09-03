import matplotlib.pyplot as plt
import numpy as np

# 1. Configuration Constants
NUM_STARS = 20000  # High star density for deep space fidelity
NUM_ARMS = 2  # Standard grand-design two-armed spiral galaxy


def generate_density_wave_3d():
    """Generates thousands of stars mapped to a 3D gravity traffic jam via vectorization."""
    # Radial distribution: cluster stars heavily near the center core
    r = np.random.uniform(0.1, 1.0, NUM_STARS) ** 1.6 * 10.0

    # Differential rotation velocities: inner stars rotate faster than outer stars
    base_angle = np.random.uniform(0, 2 * np.pi, NUM_STARS)

    # Calculate density wave position based on galactic radius
    wave_angle = base_angle - (r * 0.5)

    # Gravitational compression formula (sinusoidal velocity bottleneck)
    # This pulls stars closer together inside the wave fronts
    traffic_jam_compression = 0.35 * np.sin(NUM_ARMS * wave_angle)
    actual_angle = base_angle + traffic_jam_compression

    # 3D Galactic Bulge: Thick spherical core, paper-thin outer disk edge
    height_profile = 0.5 * np.exp(-0.4 * r) + 0.05
    z = np.random.normal(0, height_profile, NUM_STARS)

    # Convert cylindrical spatial dimensions (r, angle) into Cartesian (X, Y)
    x = r * np.cos(actual_angle)
    y = r * np.sin(actual_angle)

    # astrophysics logical mask: identify stars traveling inside high-density compression zones
    is_inside_arm = np.cos(NUM_ARMS * wave_angle) > 0.35

    # Efficient vectorized color array building
    colors = np.where(r[:, None] < 1.6, "#FFFFFF", "#DEB887")  # White core vs brown dust gaps
    colors = np.where(
        (r[:, None] >= 1.6) & is_inside_arm[:, None], "#7df9ff", colors
    )  # Insert electric blue arms
    colors = colors.flatten()

    # Size allocation vector: stars inside intense starburst zones and cores look brighter
    sizes = np.where(r < 1.6, np.random.uniform(1.0, 4.0, NUM_STARS), 0.5)
    sizes = np.where(
        (r >= 1.6) & is_inside_arm, np.random.uniform(1.2, 4.5, NUM_STARS), sizes
    )

    return x, y, z, colors, sizes


def plot_galaxy_3d_physics(x, y, z, colors, sizes):
    """Renders the stars into a highly responsive, interactive 3D space canvas."""
    fig = plt.figure(figsize=(10, 10), facecolor="#020206")

    # Initialize a hardware-accelerated 3D coordinate plot
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#020206")

    # Draw the main stellar field distribution
    ax.scatter(x, y, z, c=colors, s=sizes, alpha=0.55, edgecolors="none")

    # FIXED: Added explicit, [0], [0] arrays to place the central core glow
    ax.scatter([0], [0], [0], color="#FFFFFF", s=3000, alpha=0.15, edgecolors="none")
    ax.scatter([0], [0], [0], color="#7df9ff", s=6500, alpha=0.04, edgecolors="none")

    # Framing headers and UI configurations
    ax.set_title(
        "Interactive 3D Galactic Density Wave Theory Simulation\n"
        "(Click and drag mouse to spin and view the stellar density traffic jam)",
        color="white",
        fontsize=13,
        fontweight="bold",
        pad=10,
    )

    # Normalize axes bounds uniformly to completely eliminate spatial distortion
    max_range = np.array([x.max() - x.min(), y.max() - y.min(), 5.0]).max() / 2.0
    mid_x, mid_y = (x.max() + x.min()) * 0.5, (y.max() + y.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(-max_range / 3.5, max_range / 3.5)

    # Hide grid wires and background structural panels for realistic dark space look
    ax.grid(False)
    ax.axis("off")

    print("\nInitializing responsive 3D viewport canvas...")
    print("-> Click and drag your left mouse button to rotate and spin the galaxy.")
    print("-> Use your scroll wheel (or right-click drag) to zoom deep into the arms.")
    plt.show()


if __name__ == "__main__":
    print("Computing 20,000 vectorized orbital vectors across a 3D gravity potential...")
    x, y, z, colors, sizes = generate_density_wave_3d()
    plot_galaxy_3d_physics(x, y, z, colors, sizes)
