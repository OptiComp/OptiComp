import matplotlib.pyplot as plt
import numpy as np

from opticomp import objective_zoo

objective, search_space = objective_zoo.fetch_ackley_function()


# Generate grid data
x_range = np.linspace(search_space['param1'][0], search_space['param1'][1], 50)
y_range = np.linspace(search_space['param2'][0], search_space['param2'][1], 50)
x, y = np.meshgrid(x_range, y_range)

# Compute function values
z = np.array([[objective({'x': x_val, 'y': y_val}) for x_val, y_val in zip(row_x, row_y)] for row_x, row_y in zip(x, y)])

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Objective visualizer')
plt.show()
