import os

import matplotlib.pyplot as plt
import psutil


class WrapperResults():
    name: str
    best_params: dict[str, float]
    best_score: float
    score_history: list[float]
    elapsed_time: float
    steps: int
    cpu_history: list[float]
    ram_history: list[float]

    def __init__(self, name,
                 best_params,
                 best_score,
                 score_history,
                 elapsed_time,
                 steps,
                 cpu_history,
                 ram_history):
        self.name = name
        self.best_params = best_params
        self.best_score = best_score
        self.score_history = score_history
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

    def plot(self, show: bool = False, save_dir: str = None):
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
