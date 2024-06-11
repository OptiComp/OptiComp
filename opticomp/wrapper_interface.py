
class WrapperInterface:
    library_version = "Unknown"     # Default library version that wrapper is based on
    default_direction = "Unknown"   # Default direction

    def __init__(self, objective, search_space):
        self.__objective = objective
        self.__search_space = search_space
      
    class Config:
        Empty = "None"

    # Normalize parameters
    def _wrap_normalize_parameters(self, params, search_space):
        raise NotImplementedError("The wrapper method '_wrap_normalize_parameters' should be overridden")
    
    # Setup optimizer
    def _wrap_setup(self, objective, search_space):
        raise NotImplementedError("The wrapper method '_wrap_setup' should be overridden")
    
    # Take one optimizer step
    def _wrap_step(self, objective, search_space):
        raise NotImplementedError("The wrapper method '_wrap_step' should be overridden")
    
    # Apply optimizer
    def __optimization_loop(self, final_objective, search_space, max_steps, target_score):
        step = 0
        while True:
            step += 1
            best_params, best_value = self._wrap_step(final_objective, search_space)
            if target_score:
                if best_value >= target_score:
                    break
            if max_steps:
                if step >= max_steps:
                    break
        return best_params, best_value, step
    
    # Run optimizer
    def optimize(self, invert, max_steps=None, target_score=None):
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        
        # Create the final objective function. Normilize parameters and set the direction.
        def final_objective(params):
            params = self._wrap_normalize_parameters(params, self.__search_space)
            result = self.__objective(params)
            return -result if invert else result
        
        self._wrap_setup(final_objective, self.__search_space)

        params, score, step = self.__optimization_loop(final_objective, self.__search_space, max_steps, target_score)
        
        score = -score if invert else score
        return params, score, step
    