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

    def compare(self):
        results = {}
        for wrapper in self.wrappers:
            start_time = time.time()
            params, loss = wrapper.compare()
            elapsed_time = time.time() - start_time
            results[wrapper.__class__.__name__] = {
                'params': params,
                'loss': loss,
                'time': elapsed_time
            }
        
        best_result = min(results.items(), key=lambda x: x[1]['loss'])
        return best_result, results
