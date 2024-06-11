import time
from typing import Callable

from .wrapper_interface import WrapperInterface


# Optimizer compare class
class OptimizerSuite:
    def __init__(self, objective: Callable[[list[int]], int], search_space: dict[str, tuple[int, int]]):
        self._objective = objective
        self._search_space = search_space
        self._wrappers = []

    def add_wrapper(self, wrapper: WrapperInterface):
        # Make sure all wrappers have the same objective and search_space
        wrapper.reinitialize(self._objective, self._search_space)
        self._wrappers.append(wrapper)

    def clear_wrappers(self):
        self._wrappers.clear()

    def benchmark(self, direction: str = "minimize", max_steps: int = None, target_score: int = None, verbose: bool = True):
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        results = {}
        for wrapper in self._wrappers:
            start_time = time.time()
            params, score, step = wrapper.optimize(direction, max_steps, target_score)
            elapsed_time = time.time() - start_time
            results[wrapper.__class__.__name__] = {
                'params': params,
                'score': score,
                'time': elapsed_time,
                'steps': step
            }

            if verbose:
                print(f"Optimiser: {wrapper.__class__.__name__}")
                print(f"Score: {score}")
                print(f"Time: {elapsed_time}")
                print(f"steps: {step}\n")
        
        best_result = min(results.items(), key=lambda x: x[1]['score'])
        return best_result, results
    
    def get_best():
        raise NotImplementedError()
