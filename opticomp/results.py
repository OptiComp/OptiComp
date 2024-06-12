from .wrapper_interface import WrapperInterface


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
        """
        Summarize the results for this wrappers.
        """
        print(f"Optimiser: {self.name}")
        print(f"Score: {self.best_score}")
        print(f"Time: {self.elapsed_time}")
        print(f"steps: {self.steps}\n")


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

    def _normalize_name(self, name):
        norm_name = name.lower().replace(" ", "").replace("_", "").replace("-", "")
        return norm_name

    def summarize(self, wrapper_name: str):
        """
        Summarize the results for a specific wrapper.
        
        Parameters
        ----------
        wrapper_name : str
            Provide the wrapper name you want to summarize.
        """
        for result in self._results:
            if result.name.lower() == self._normalize_name(wrapper_name):
                result.summarize()
                return
        print(f"No results found for optimizer: {wrapper_name}")

    def summarize_all(self):
        """
        Summarize the results for all wrappers.
        """
        for result in self._results:
            result.summarize()

    def fetch_wrapper_result(self, wrapper_name: str) -> WrapperResult:
        """
        Fetch and return the result class of a specific wrapper
        
        Parameters
        ----------
        wrapper_name : str
            Provide the wrapper name you want to summarize.

        Returns
        -------
        class WrapperResult
            A class containing the results for a specific wrapper
        """
        for result in self._results:
            if result.name.lower() == self._normalize_name(wrapper_name):
                return result
        print(f"No results found for wrapper: {wrapper_name}")
        # Create and return a default WrapperResult
        return WrapperResult("EmptyResult", None, None, None, None, None)
