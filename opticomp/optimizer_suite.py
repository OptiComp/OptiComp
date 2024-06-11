import time

# from . import wrappers_control


# Optimizer compare class
class OptimizerSuite:
    def __init__(self, objective, search_space):
        self._objective = objective
        self._search_space = search_space
        self._wrappers = []

    def add_wrapper(self, wrapper):
        # Make sure all wrappers have the same objective and search_space
        wrapper.reinitialize(self._objective, self._search_space)
        self._wrappers.append(wrapper)

    def clear_wrappers(self):
        self._wrappers.clear()

    def benchmark(self, direction="minimize", max_steps=None, target_score=None, verbose=True):
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        results = {}
        for wrapper in self._wrappers:
            invert = False
            if wrapper.default_direction != direction:
                invert = True
            start_time = time.time()
            params, score, step = wrapper.optimize(invert, max_steps, target_score)
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
        print("Not made yet")
