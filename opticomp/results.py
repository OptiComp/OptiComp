from .wrapper_interface import WrapperInterface


class BenchmarkResults():
    def __init__(self):
        self._results = []

    def _add_result(self, wrapper,
                    best_params,
                    best_score,
                    elapsed_time,
                    steps):
        result = WrapperResult(wrapper.__class__.__name__,
                                wrapper,
                                best_params,
                                best_score,
                                elapsed_time,
                                steps)
        self._results.append(result)

    def summarize(self, wrapper_name: str):
        for result in self._results:
            if result.name.lower() == wrapper_name.lower():
                result.summarize()
                return
        print(f"No results found for optimizer: {wrapper_name}")

    def summarize_all(self):
        for result in self._results:
            result.summarize()

    def fetch_wrapper_result(self, wrapper_name: str):
        for result in self._results:
            if result.name.lower() == wrapper_name.lower():
                return result
        print(f"No results found for wrapper: {wrapper_name}")
        # Create and return a default WrapperResult
        return WrapperResult("EmptyResult", None, None, None, None, None)


class WrapperResult():
    name: str
    wrapper: WrapperInterface
    best_params: dict[str, float]
    best_score: int
    elapsed_time: int
    steps: int

    def __init__(self, name,
                 wrapper,
                 best_params,
                 best_score,
                 elapsed_time,
                 steps):
        self.name = name
        self.wrapper = wrapper
        self.best_params = best_params
        self.best_score = best_score
        self.elapsed_time = elapsed_time
        self.steps = steps
    
    def summarize(self):
        print(f"Optimiser: {self.name}")
        print(f"Score: {self.best_score}")
        print(f"Time: {self.elapsed_time}")
        print(f"steps: {self.steps}\n")



