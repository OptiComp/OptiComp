# Wrapper interface
class WrapperInterface:   
    name = "Unknown"                # Default name for the wrapper
    library_version = "Unknown"     # Default library version that wrapper is based on
    default_direction = "Unknown"   # Default direction

    def __init__(self, objective, search_space):
        self.objective = objective
        self.search_space = search_space
      
    class Config:
        Empty = "None"

    def _wrap_norm_parameters(self, params):
        raise NotImplementedError("This method should be overridden to normalize the parameters for the objective")

    def _wrap_execute_optimization(self, final_objective, n_steps):
        raise NotImplementedError("This method should be overridden by subclasses")
    
    def optimize(self, invert, n_steps):
        # Create the final objective function. Normilize parameters and set the direction. 
        def final_objective(params):
            # Normalize parameters
            params = self._wrap_norm_parameters(params)
            result = self.objective(params)
            # Invert result if needed
            return -result if invert else result

        # Run optimizer
        params, score = self._wrap_execute_optimization(final_objective, n_steps)
        
        # Invert final score if needed
        score = -score if invert else score
        return params, score
    