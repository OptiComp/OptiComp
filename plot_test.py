import matplotlib.pyplot as plt
import numpy as np


# Define the Ackley objective function
def objective(params: dict[str, float]) -> float:
    x = np.array(list(params.values()))
    n = len(x)
    return -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / n)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / n) + 20 + np.e

# Define the search space for 4 dimensions
search_space = {
    'x1': (-32.768, 32.768),
    'x2': (-32.768, 32.768),
    'x3': (-32.768, 32.768),
    'x4': (-32.768, 32.768)
}

# Fixed parameters for creating a 2D slice
fixed_params = {'x3': 0, 'x4': 0}

# Example optimizer path (replace with actual optimizer path)
optimizer_path = [
    {'x1': 30, 'x2': 30, 'x3': 0, 'x4': 0},
    {'x1': 20, 'x2': 20, 'x3': 0, 'x4': 0},
    {'x1': 10, 'x2': 10, 'x3': 0, 'x4': 0},
    {'x1': 5, 'x2': 5, 'x3': 0, 'x4': 0},
    {'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0}
]


# Function to visualize optimizer path on 2D slices
def visualize_optimizer_path_2d_slice(dim1, dim2):
    x_dim1 = np.linspace(search_space[dim1][0], search_space[dim1][1], 50)
    x_dim2 = np.linspace(search_space[dim2][0], search_space[dim2][1], 50)
    x, y = np.meshgrid(x_dim1, x_dim2)
    
    z = np.zeros_like(x)
    for i in range(len(x_dim1)):
        for j in range(len(x_dim2)):
            params = {dim1: x_dim1[i], dim2: x_dim2[j]}
            params.update(fixed_params)
            z[j, i] = objective(params)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.contourf(x, y, z, levels=50, cmap='viridis')
    
    path_x = [point[dim1] for point in optimizer_path]
    path_y = [point[dim2] for point in optimizer_path]
    ax.plot(path_x, path_y, marker='o', color='r', label='Optimizer Path')
    
    ax.set_xlabel(dim1)
    ax.set_ylabel(dim2)
    ax.set_title(f'Ackley Function 2D Slice ({dim1}, {dim2}) with Optimizer Path')
    ax.legend()
    
    plt.show()

# Example usage: Visualize optimizer path on a slice defined by x1 and x2
visualize_optimizer_path_2d_slice('x1', 'x2')
