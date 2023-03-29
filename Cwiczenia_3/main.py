import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
grav = 10
pendulum_length = 1.0

initial_angle = math.pi / 4
initial_velocity = 0.0

max_time = 5
time_step = 0.01
steps = int(max_time / time_step) + 1


def ang_accel(angle):
    return -grav / pendulum_length * math.sin(angle)


def euler_method(init_angle, init_velocity, time_step):
    time = 0.0
    angle = init_angle
    velocity = init_velocity

    time_values = [time]
    angle_values = [angle]
    velocity_values = [velocity]

    for i in range(steps):
        accel = ang_accel(angle)

        angle += velocity * time_step
        velocity += accel * time_step

        time += time_step

        time_values.append(time)
        angle_values.append(angle)
        velocity_values.append(velocity)

    return time_values, angle_values, velocity_values, "Euler Method"


def midpoint_method(init_angle, init_velocity, time_step):
    time = 0.0
    angle = init_angle
    velocity = init_velocity

    time_values = [time]
    angle_values = [angle]
    velocity_values = [velocity]

    for i in range(steps):
        mid_angle = angle + 0.5 * velocity * time_step
        mid_velocity = velocity + 0.5 * ang_accel(angle) * time_step
        mid_accel = ang_accel(mid_angle)

        angle += mid_velocity * time_step
        velocity += mid_accel * time_step

        time += time_step

        time_values.append(time)
        angle_values.append(angle)
        velocity_values.append(velocity)

    return time_values, angle_values, velocity_values, "Midpoint Method"


def runge_kutta_2(init_angle, init_velocity, time_step):
    time = 0.0
    angle = init_angle
    velocity = init_velocity

    time_values = [time]
    angle_values = [angle]
    velocity_values = [velocity]

    for i in range(steps):
        accel1 = ang_accel(angle)

        mid_angle = angle + 0.5 * velocity * time_step
        mid_velocity = velocity + 0.5 * accel1 * time_step
        accel2 = ang_accel(mid_angle)

        angle += mid_velocity * time_step
        velocity += accel2 * time_step

        time += time_step

        time_values.append(time)
        angle_values.append(angle)
        velocity_values.append(velocity)

    return time_values, angle_values, velocity_values, "Runge-Kutta 2 Method"


def display_energy(time_values, angle_values, velocity_values, pendulum_length, mass, method):
    angle_values = np.array(angle_values)
    velocity_values = np.array(velocity_values)

    kinetic_energy = 0.5 * mass * (pendulum_length * velocity_values) ** 2

    potential_energy = mass * 9.81 * pendulum_length * (1 - np.cos(angle_values))

    total_energy = kinetic_energy + potential_energy

    plt.plot(time_values, kinetic_energy, label=f'{method} - Kinetic Energy')
    plt.plot(time_values, potential_energy, label=f'{method} - Potential Energy')
    plt.plot(time_values, total_energy, label=f'{method} - Total Energy')
    plt.legend()
    plt.title(f'Energy of a Pendulum over Time - {method}')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.show()


def plot_trajectory(angle_values, pendulum_length, method):
    x_values = pendulum_length * np.sin(angle_values)
    y_values = -pendulum_length * np.cos(angle_values)

    plt.plot(x_values, y_values, label=f'{method} - Trajectory')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.legend()
    plt.title(f'Trajectory of a Pendulum - {method}')
    plt.show()

def main():
    # Pendulum parameters
    pendulum_length = 1.0
    mass = 1.0
    initial_angle = np.pi / 4
    initial_velocity = 0.0
    time_step = 0.01

    time_euler, angle_euler, velocity_euler, method_euler = euler_method(initial_angle, initial_velocity, time_step)

    display_energy(time_euler, angle_euler, velocity_euler, pendulum_length, mass, method_euler)
    plot_trajectory(angle_euler, pendulum_length, method_euler)

    time_midpoint, angle_midpoint, velocity_midpoint, method_midpoint = midpoint_method(initial_angle, initial_velocity, time_step)

    display_energy(time_midpoint, angle_midpoint, velocity_midpoint, pendulum_length, mass, method_midpoint)
    plot_trajectory(angle_midpoint, pendulum_length, method_midpoint)

    time_rk2, angle_rk2, velocity_rk2, method_rk2 = runge_kutta_2(initial_angle, initial_velocity, time_step)

    display_energy(time_rk2, angle_rk2, velocity_rk2, pendulum_length, mass, method_rk2)
    plot_trajectory(angle_rk2, pendulum_length, method_rk2)


if __name__ == "__main__":
    main()