import os

import matplotlib.pyplot as plt


class WrapperResults():
    name: str
    params: dict[str, float]
    score: float
    history: list
    elapsed_time: float
    steps: int

    def __init__(self, name,
                 params,
                 score,
                 history,
                 elapsed_time,
                 steps):
        self.name = name
        self.params = params
        self.score = score
        self.history = history
        self.elapsed_time = elapsed_time
        self.steps = steps
    
    def summarize(self):
        """
        Summarize the results for this wrappers.
        """
        print(f"Optimiser: {self.name}")
        print(f"Score: {self.score}")
        print(f"Time: {self.elapsed_time}")
        print(f"steps: {self.steps}\n")

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

        if show:
            plt.show()
        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
            file_path = os.path.join(save_dir, f"plot_{self.name}.png")
            plt.savefig(file_path)
