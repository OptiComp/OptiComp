# Imports
import time

# Optimizer compare class
class OptimizerCompare:
    def __init__(self, objective, search_space):
        self.objective = objective
        self.search_space = search_space
        self.wrappers = []

    def add_wrapper(self, wrapper_class):
        wrapper = wrapper_class(self.objective, self.search_space)
        self.wrappers.append(wrapper)

    def clear_wrappers(self):
        self.wrappers.clear()

    def compare(self, direction="minimize", n_steps=100, verbose=True):
        results = {}
        for wrapper in self.wrappers:
            # Check optimizer direction
            invert = False
            if wrapper.default_direction != direction:
                invert = True
            # Set start time
            start_time = time.time()
            params, score = wrapper._run(invert, n_steps)
            elapsed_time = time.time() - start_time
            results[wrapper.name] = {
                'params': params,
                'score': score,
                'time': elapsed_time
            }

            if verbose:
                print(f"Optimiser: {wrapper.name}")
                print(f"Score: {score}")
                print(f"Time: {elapsed_time}\n")
        
        best_result = min(results.items(), key=lambda x: x[1]['score'])
        return best_result, results
