from typing import Callable

from .result_benchmark import BenchmarkResults
from .wrapper_interface import WrapperInterface


# Optimizer compare class
class BenchmarkSuite:
    """
    A class for comparing and benchmarking optimization wrappers.

    Parameters
    ----------
    objective : Callable[[dict[str, float]], float]
        The objective function to be optimized.
    search_space : dict[str, tuple[float, float]
        The search space defining the range of each parameter.

    Methods
    -------
    add_wrapper(wrapper)
        tuple
            A tuple containing the following elements:)
        Add a wrapper to the BenchmarkSuite.

    clear_wrappers()
        Clear all wrappers from the BenchmarkSuite.

    benchmark(direction = "minimize", max_steps = None, target_score = None, verbose = True)
        Benchmark wrappers on provided objective and search_space.

    get_best()
        [Not Implemented] Get the best result from the benchmark.
    """

    def __init__(self, objective: Callable[[dict[str, float]], float], search_space: dict[str, tuple[float, float]]):
        self.objective = objective
        self.search_space = search_space
        self._wrappers = []

    def add_wrapper(self, wrapper: WrapperInterface):
        """
        Add a wrapper to the BenchmarkSuite.

        Parameters
        ----------
        wrapper : WrapperInterface
            The wrapper to be added. Can be from wrapper_zoo or custom.
        """
        # Make sure all wrappers have the same objective and search_space
        wrapper.reinitialize(self.objective, self.search_space)
        self._wrappers.append(wrapper)

    def clear_wrappers(self):
        """
        Clear all wrappers from the BenchmarkSuite.
        """
        self._wrappers.clear()

    def benchmark(self, direction: str, n_runs: int = 5, max_steps: int = None, target_score: float = None, verbose: bool = False, progress_bar: bool = False) -> BenchmarkResults:
        """
        Benchmark wrappers on provided objective and search_space.

        Parameters
        ----------
        direction : str, optional
            The direction of optimization. Default is 'minimize'.
        n_runs : int, optional
            Set the amount of times each optimizer is run. More runs provides a more reliable outcome, but takes longer.
        max_steps : int, optional
            The maximum number of optimization steps. If not provided, target_score must be provided.
        target_score : float, optional
            The target score to achieve. If not provided, max_steps must be provided.
        verbose : bool, optional
            If True, print information during benchmarking. Default is False.
        progress_bar: bool, optional
            If True, a progress bar will be shown during benchmarking. Default is False.

        Returns
        -------
        class BenchmarkResults
            A class containing all benchmark results
        """
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        if direction not in {'minimize', 'maximize'}:
            raise ValueError(f"Unknown direction: '{direction}'. Please choose 'minimize' or 'maximize'.")
        
        results = BenchmarkResults()

        for wrapper in self._wrappers:
            if verbose or progress_bar:
                print(f"\n=== Wrapper: {wrapper.__class__.__name__} === {n_runs} runs of max {max_steps} steps.")

            results_run = []
            for _ in range(n_runs):
                wrapper_result = wrapper.optimize(direction, max_steps=max_steps, target_score=target_score, progress_bar=progress_bar)
                results_run.append(wrapper_result)
                print(f"\nScore: {wrapper_result.best_score}")

            results._add_result(results_run)

            if verbose:
                print(f"\nScore: {wrapper_result.best_score}")
                print(f"Time: {wrapper_result.elapsed_time}")
                print(f"steps: {wrapper_result.steps}")
        
        if verbose:
            print()
        
        return results
    
    def get_best():
        raise NotImplementedError("This feature will be introduced in future versions of the library.")
