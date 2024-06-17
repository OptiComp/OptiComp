
class WrapperResults():
    name: str
    params: dict[str, float]
    score: float
    elapsed_time: float
    steps: int

    def __init__(self, name,
                 params,
                 score,
                 elapsed_time,
                 steps):
        self.name = name
        self.params = params
        self.score = score
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
