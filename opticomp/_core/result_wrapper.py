import os

import matplotlib.pyplot as plt


class WrapperResults():
    name: str
    best_params: dict[str, float]
    best_score: float
    history: list
    elapsed_time: float
    steps: int
    cpu_usage: list[float]
    ram_usage: list[float]

    def __init__(self, name,
                 best_params,
                 best_score,
                 history,
                 elapsed_time,
                 steps,
                 cpu_usage,
                 ram_usage):
        self.name = name
        self.best_params = best_params
        self.best_score = best_score
        self.history = history
        self.elapsed_time = elapsed_time
        self.steps = steps
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
    
    def summarize(self):
        """
        Summarize the results for this wrappers.
        """
        avr_cpu = sum(self.cpu_usage) / len(self.cpu_usage) if self.cpu_usage else 0.0
        avr_ram = sum(self.ram_usage) / len(self.ram_usage) if self.ram_usage else 0.0

        print(f"Optimiser: {self.name}")
        print(f"Score: {self.best_score}")
        print(f"Time: {self.elapsed_time}")
        print(f"steps: {self.steps}")
        print(f"avr CPU usage: {avr_cpu:.1f}%")
        print(f"avr RAM usage: {avr_ram:.1f}\n")
        print(self.cpu_usage)

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
        y = self.history
        for step in range(len(self.history)):
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
