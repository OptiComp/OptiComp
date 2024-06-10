# Wrapper interface
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
        raise NotImplementedError("This method should be overridden to normalize the parameters for the objective")

    # Setup optimizer
    def _wrap_setup(self, objective, search_space):
        raise NotImplementedError("This method should be overridden")
    
    # Take one optimizer step
    def _wrap_step(self, objective, search_space):
        raise NotImplementedError("This method should be overridden")
    
    # Apply optimizer
    def __optimization_loop(self, final_objective, search_space, max_steps, target_value):
        step = 0
        while True:
            step += 1
            # Perform optimizer
            best_params, best_value = self._wrap_step(final_objective, search_space)
            # Stop when target_value is reached
            if target_value:
                if best_params >= target_value:
                    break
            # Stop when max_steps is reached
            if max_steps:
                if step >= max_steps:
                    break
        return best_params, best_value
    
    # Run optimizer
    def optimize(self, invert, max_steps=None, target_value=None):
        if not max_steps and not target_value:
            raise ValueError("Either max_steps or target_value must be provided")
        
        # Create the final objective function. Normilize parameters and set the direction.
        def final_objective(params):
            # Normalize parameters
            params = self._wrap_normalize_parameters(params, self.__search_space)
            result = self.__objective(params)
            # Invert result if needed
            return -result if invert else result
        
        # Setup optimizer
        self._wrap_setup(final_objective, self.__search_space)

        # Run optimizer
        params, score = self.__optimization_loop(final_objective, self.__search_space, max_steps, target_value)
        
        # Invert final score if needed
        score = -score if invert else score
        return params, score
    