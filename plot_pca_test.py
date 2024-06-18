import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

# Example optimizer path in higher-dimensional space
optimizer_path = [
    {'x1': 30, 'x2': 30, 'x3': 0, 'x4': 0},
    {'x1': 20, 'x2': 20, 'x3': 0, 'x4': 0},
    {'x1': 10, 'x2': 10, 'x3': 0, 'x4': 0},
    {'x1': 5, 'x2': 5, 'x3': 0, 'x4': 0},
    {'x1': 0, 'x2': 0, 'x3': 0, 'x4': 0}
]


# Example function to retrieve objective value
def objective(params):
    x = np.array(list(params.values()))
    n = len(x)
    return -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / n)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / n) + 20 + np.e

# Convert optimizer path to numpy array
optimizer_path_array = np.array([[point['x1'], point['x2'], point['x3'], point['x4']] for point in optimizer_path])

# Perform PCA on optimizer path
pca = PCA(n_components=2)
optimizer_path_pca = pca.fit_transform(optimizer_path_array)

# Plot optimizer path in PCA space
plt.figure()
plt.plot(optimizer_path_pca[:, 0], optimizer_path_pca[:, 1], marker='o', color='r')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Optimizer Path in PCA Space')
plt.grid(True)
plt.show()
