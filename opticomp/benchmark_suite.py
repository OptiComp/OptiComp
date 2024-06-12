import time
from typing import Callable

from .wrapper_interface import WrapperInterface
from . results import BenchmarkResults


# Optimizer compare class
class BenchmarkSuite:
    """
    A class for comparing and benchmarking optimization wrappers.

    Parameters
    ----------
    objective : Callable[[list[int]], int]
        The objective function to be optimized.
    search_space : dict[str, tuple[int, int]]
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

    def __init__(self, objective: Callable[[list[int]], int], search_space: dict[str, tuple[int, int]]):
        self._objective = objective
        self._search_space = search_space
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
        wrapper.reinitialize(self._objective, self._search_space)
        self._wrappers.append(wrapper)

    def clear_wrappers(self):
        """
        Clear all wrappers from the BenchmarkSuite.
        """
        self._wrappers.clear()

    def benchmark(self, direction: str = "minimize", max_steps: int = None, target_score: int = None, verbose: bool = True):
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
            If True, print detailed information during benchmarking. Default is True.

        Returns
        -------
        class BenchmarkResults
            A class containing all benchmark results
        """
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        
        results = BenchmarkResults()

        for wrapper in self._wrappers:
            start_time = time.time()
            params, score, steps = wrapper.optimize(direction, max_steps, target_score)
            elapsed_time = time.time() - start_time

            results._add_result(wrapper, params, score, elapsed_time, steps)

            if verbose:
                print(f"Optimiser: {wrapper.__class__.__name__}")
                print(f"Score: {score}")
                print(f"Time: {elapsed_time}")
                print(f"steps: {steps}\n")
        
        return results
    
    def get_best():
        raise NotImplementedError()
