import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lorenz_system(sigma=10, rho=28, beta=8/3):
    """
    Defines the Lorenz system of differential equations.
    
    Parameters:
    - sigma, rho, beta: Parameters defining the Lorenz attractor dynamics.
    
    Returns:
    A function suitable for integration that represents the Lorenz equations.
    """
    def lorenz(t, state):
        x, y, z = state
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return [dx_dt, dy_dt, dz_dt]
    return lorenz

def simulate_lorenz_attractor(initial_conditions, t_span, lorenz_func):
    """
    Solves the Lorenz attractor ODEs and returns the solution.
    
    Parameters:
    - initial_conditions: Starting point for the Lorenz attractor.
    - t_span: Time interval for the simulation.
    - lorenz_func: Function defining the Lorenz equations.
    
    Returns:
    Solution object containing the trajectory of the Lorenz attractor.
    """
    sol = solve_ivp(lorenz_func, t_span, initial_conditions, dense_output=True)
    return sol

def extract_samples_from_lorenz(solution, dimension=0, num_samples=1000):
    """
    Samples points from the Lorenz attractor solution.
    
    Parameters:
    - solution: Solution object from the Lorenz attractor simulation.
    - dimension: Which dimension to sample from (default 0, i.e., x-coordinate).
    - num_samples: Number of samples to take.
    
    Returns:
    Array of sampled points.
    """
    sample_points = solution.sol(np.linspace(*t_span, num_samples))
    return sample_points[:, dimension]

def iterate_logistic_map(inputs, r_logistic=3.9, initial_x=0.5):
    """
    Iterates the logistic map using inputs and returns the sequence.
    
    Parameters:
    - inputs: Sequence of inputs to drive the logistic map.
    - r_logistic: Parameter for the logistic map.
    - initial_x: Initial value for the logistic map.
    
    Returns:
    List containing the logistic map sequence.
    """
    logistic_sequence = [initial_x]
    for input_x in inputs:
        next_x = r_logistic * input_x * (1 - input_x)
        logistic_sequence.append(next_x)
    return logistic_sequence

def visualize_results(lorenz_solution, logistic_sequence):
    """
    Plots the Lorenz attractor and the logistic map sequence.
    """
    plt.figure(figsize=(12, 6))

    # Lorenz Attractor 3D plot
    ax = plt.subplot(1, 2, 1, projection='3d')
    ax.plot(lorenz_solution.y[0], lorenz_solution.y[1], lorenz_solution.y[2])
    ax.set_title('Lorenz Attractor')

    # Logistic Map plot
    plt.subplot(1, 2, 2)
    plt.plot(logistic_sequence, label='Logistic Map Sequence', color='C1')
    plt.xlabel('Iteration')
    plt.ylabel('x_n')
    plt.title('Logistic Map Output Influenced by Lorenz Attractor')
    plt.legend()

    plt.show()

# Parameters and Initial Conditions
sigma, rho, beta = 10, 28, 8/3
initial_conditions_lorenz = [1, 1, 1]
t_span = (0, 100)
r_logistic = 3.9
x0_logistic = 0.5

# Main Execution
lorenz_func = lorenz_system(sigma, rho, beta)
lorenz_solution = simulate_lorenz_attractor(initial_conditions_lorenz, t_span, lorenz_func)
lorenz_x_samples = extract_samples_from_lorenz(lorenz_solution)
logistic_sequence = iterate_logistic_map(lorenz_x_samples)

# Visualization
visualize_results(lorenz_solution, logistic_sequence)
