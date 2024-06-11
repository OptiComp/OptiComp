import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Callable

import psutil

from .wrapper_interface import WrapperInterface

'''
Multiprocessing does work, HOWEVER.
Some optimizers dont play well together.
Specifically the bayesian optimizer can not run twice at the same time.
If you run 1, CPU 40%.
If you run 2 CPU 100%.
This is with an Intel I5, but still.

Currently the code checks if the CPU is below a set threshold before starting a new process.
However, it will start another process when the CPU is under 40% and it will not stop untill finished.

This ofcourse causes the elapsed time for these optimizers to be way higher.
'''


def benchmark_wrapper(wrapper, direction, max_steps, target_score):
    start_time = time.time()
    params, score, step = wrapper.optimize(direction, max_steps, target_score)
    print("DONE")
    elapsed_time = time.time() - start_time
    return wrapper.__class__.__name__, {
        'params': params,
        'score': score,
        'time': elapsed_time,
        'steps': step
        }


# Optimizer compare class
class OptimizerSuite:
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
        Add a wrapper to the OptimizerSuite.

    clear_wrappers()
        Clear all wrappers from the OptimizerSuite.

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
        Add a wrapper to the OptimizerSuite.

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
        Clear all wrappers from the OptimizerSuite.
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
        tuple
            A tuple containing the following elements:
            - a tuple containing the best result
            - a tuple containing the all results
        """
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        
        results = {}
        with ProcessPoolExecutor(max_workers=10) as executor:
            futures = {}
            for wrapper in self._wrappers:
                # Wait if CPU usage is too high before submitting a new task
                while psutil.cpu_percent(interval=0.1) > 70:
                    time.sleep(0.5)
                print("Start process")
                future = executor.submit(benchmark_wrapper, wrapper, direction, max_steps, target_score)
                futures[future] = wrapper
                # Wait a few seconds for previous optimizer to start before checking cpu
                time.sleep(2)
            
            for future in as_completed(futures):
                name, result = future.result()
                results[name] = result
                if verbose:
                    print(f"Optimiser: {name}")
                    print(f"Score: {result['score']}")
                    print(f"Time: {result['time']}")
                    print(f"Steps: {result['steps']}\n")
        
        best_result = min(results.items(), key=lambda x: x[1]['score'])
        return best_result, results
    
    def get_best():
        raise NotImplementedError()
