import time
from typing import Callable

from ..wrapper_zoo.wrapper_interface import WrapperInterface
from .results import BenchmarkResults


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
        wrapper.initialize(self.objective, self.search_space)
        self._wrappers.append(wrapper)

    def clear_wrappers(self):
        """
        Clear all wrappers from the BenchmarkSuite.
        """
        self._wrappers.clear()

    def benchmark(self, direction: str = "minimize", max_steps: int = None, target_score: int = None, verbose: bool = True, progress_bar: bool = False):
        """
        Benchmark wrappers on provided objective and search_space.

        Parameters
        ----------
        direction : str, optional
            The direction of optimization. Default is 'minimize'.
        max_steps : int, optional
            The maximum number of optimization steps. If not provided, target_score must be provided.
        target_score : int, optional
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
        
        results = BenchmarkResults()

        for wrapper in self._wrappers:
            if verbose or progress_bar:
                print(f"\n=== Wrapper: {wrapper.__class__.__name__} ===")

            start_time = time.time()
            params, score, steps = wrapper.optimize(direction, max_steps=max_steps, target_score=target_score, progress_bar=progress_bar)
            elapsed_time = time.time() - start_time

            results._add_result(wrapper, params, score, elapsed_time, steps)

            if verbose:
                print(f"\nScore: {score}")
                print(f"Time: {elapsed_time}")
                print(f"steps: {steps}")
        
        if verbose:
            print()
        
        return results
    
    def get_best():
        raise NotImplementedError()
