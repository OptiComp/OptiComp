# Wrapper interface
class WrapperInterface: 
    def __init__(self, objective, search_space):
        self.objective = objective
        self.search_space = search_space

    def _wrap_norm_parameters(self, params):
        raise NotImplementedError("This method should be overridden to normalize the parameters for the objective")

    def _wrap_execute_optimization(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def optimize(self, invert, n_steps):
        # Create the final objective function. Normilize parameters and set the direction. 
        def final_objective(params):
            params = self._wrap_norm_parameters(params)
            result = self.objective(params)
            # Invert result
            if invert:
                return -result
            else:
                return result
        # Run optimizer
        params, score = self._wrap_execute_optimization(final_objective, n_steps)
        # Invert final score
        if invert:
            score = -score
        return params, score