import os
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
import psutil


class WrapperResults():
    name: str
    objective: Callable[[dict[str, float]], float]
    search_space: dict[str, tuple[float, float]]
    best_params: dict[str, float]
    best_score: float
    score_history: list[float]
    params_history: list[dict[str, float]]
    elapsed_time: float
    steps: int
    cpu_history: list[float]
    ram_history: list[float]

    def __init__(self, name,
                 objective = None,
                 search_space = None,
                 best_params = None,
                 best_score = None,
                 score_history = None,
                 params_history = None,
                 elapsed_time = None,
                 steps = None,
                 cpu_history = None,
                 ram_history = None):
        self.name = name
        self.objective = objective
        self.search_space = search_space
        self.best_params = best_params
        self.best_score = best_score
        self.score_history = score_history
        self.params_history = params_history
        self.elapsed_time = elapsed_time
        self.steps = steps
        self.cpu_history = cpu_history
        self.ram_history = ram_history
    
    def summarize(self):
        """
        Summarize the results for this wrappers.
        """
        avr_cpu = sum(self.cpu_history) / len(self.cpu_history) if self.cpu_history else 0.0
        avr_ram = sum(self.ram_history) / len(self.ram_history) if self.ram_history else 0.0
        peak_cpu_usage = max(self.cpu_history) if self.cpu_history else 0.0
        peak_ram_usage = max(self.ram_history) if self.ram_history else 0.0
        
        print(f"\n=== Wrapper: {self.name} ===")
        print(f"Score: {self.best_score}")
        print(f"Time: {self.elapsed_time:.4f} sec")
        print(f"steps: {self.steps}")
        print("=== System")
        print(f"avr CPU usage: {avr_cpu:.1f}% over {psutil.cpu_count()} cores")
        print(f"peak CPU usage: {peak_cpu_usage:.1f}% over {psutil.cpu_count()} cores")
        print(f"avr RAM usage: {avr_ram:.1f} mb")
        print(f"peak RAM usage: {peak_ram_usage:.1f} mb\n")

    def plot_score(self, show: bool = False, save_dir: str = None):
        """
        Plot a graph to visualize the wrapper history.
        
        Parameters
        ----------
        show : bool = False, optional
            Set to true to show the graph.
        save_dir: str = None. optional
            Give a dir to save the graph to.
        """
        x = []
        y = self.score_history
        for step in range(len(self.score_history)):
            x.append(step + 1)

        plt.figure()
        plt.plot(x, y)
        plt.title(self.name)
        plt.xlabel('Steps')
        plt.ylabel('Score')

        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
            file_path = os.path.join(save_dir, f"plot_{self.name}.png")
            plt.savefig(file_path)
        if show:
            plt.show()

    def plot_objective_landscape(self, params, show_path=False, fixed_params=None, resolution=50, show: bool = False, save_dir: str = None):
        """
        Plot the landscape of the objective function.

        !!!WARNING!!!
        If your objective function is slow, this will take a long time.

        Parameters
        ----------
        params : list
            The names of the params you want to map.
        resolution : int, optional
            The number of points to sample in each dimension (default is 50).
        show : bool, optional
            Set to True to show the plot.
        save_dir : str, optional
            Directory to save the plot.
        """
        if len(params) != 2:
            raise ValueError("Currently, only 2D plots are supported. Please provide exactly two parameters to vary.")
        
        fixed_params = {}
        for name in self.search_space:
            if name not in params:
                fixed_params[name] = self.best_params[name]
        param1, param2 = params
        range1, range2 = self.search_space[param1], self.search_space[param2]

        x = np.linspace(range1[0], range1[1], resolution)
        y = np.linspace(range2[0], range2[1], resolution)
        x, y = np.meshgrid(x, y)

        z = np.zeros_like(x)
        for i in range(resolution):
            for j in range(resolution):
                params = {param1: x[i, j], param2: y[i, j]}
                if fixed_params:
                    params.update(fixed_params)
                z[i, j] = self.objective(params)

        plt.figure()
        plt.contourf(x, y, z, levels=50, cmap='viridis')
        plt.colorbar(label='Score')
        plt.title(f"Objective Landscape for {self.name}")
        plt.xlabel(param1)
        plt.ylabel(param2)

        if show_path:
            path_x = [point[param1] for point in self.params_history]
            path_y = [point[param2] for point in self.params_history]
            plt.plot(path_x, path_y, '-o', color='orange', label='Optimizer Path', zorder=1)

        best_param1 = self.best_params[param1]
        best_param2 = self.best_params[param2]
        plt.scatter(best_param1, best_param2, color='r', label='Best Score', zorder=2)

        plt.legend()

        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
            file_path = os.path.join(save_dir, f"landscape_{self.name}.png")
            plt.savefig(file_path)
        if show:
            plt.show()
