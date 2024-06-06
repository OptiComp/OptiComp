# Wrapper interface
class WrapperInterface: 
    def __init__(self, objective, search_space):
        self.objective = objective
        self.search_space = search_space

    def norm_parameters(self, params):
        raise NotImplementedError("This method should be overridden to normalize the parameters for the objective")
    
    # def reverse_objective(self):
    #     def reversed(params):
    #         return -self.norm_objective(params)
    #     self.norm_objective = reversed

    def optimize(self):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def _run(self, invert):
        # Create the final objective function. Normilize parameters and set the direction. 
        def final_objective(params):
            params = self.norm_parameters(params)
            result = self.objective(params)
            # Invert result
            if invert:
                return -result
            else:
                return result
        # Run optimizer
        params, score = self.optimize(final_objective)
        # Invert final score
        if invert:
            score = -score
        # Normilize final parameters
        # norm_params = self.norm_parameters(params)
        # Return final parameters and result
        return params, score