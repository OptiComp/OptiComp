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

    def plot(self):

        step = 0
        x = []
        y = []
        for score in self.history:
            step += 1
            x.append(step)
            y.append(score)

        plt.figure()
        plt.plot(x, y)
        plt.title(self.name)
        plt.xlabel('Steps')
        plt.ylabel('Score')

        # Show the plot
        plt.show()
