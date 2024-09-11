import matplotlib.pyplot as plt
import numpy as np

def calculate_velocity(time, mass, gravity, drag_coefficient, air_density):
    velocity = np.sqrt((2 * mass * gravity) / (drag_coefficient * air_density)) * (1 - np.exp((-drag_coefficient * air_density * time) / mass))
    return velocity

def plot_velocity(time, velocity):
    plt.plot(time, velocity)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity of Falling Object with Air Resistance')
    plt.grid(True)
    plt.show()

# Constants
mass = 1.0  # kg
gravity = 9.8  # m/s^2
drag_coefficient = 0.5
air_density = 1.2  # kg/m^3

# Time range
time = np.linspace(0, 10, 100)

# Calculate velocity
velocity = calculate_velocity(time, mass, gravity, drag_coefficient, air_density)

# Plot velocity
plot_velocity(time, velocity)
# The plot will show the velocity of a falling object with air resistance over time. The velocity decreases as the object falls due to the drag force acting against it.