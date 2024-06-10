import logging

import optuna


# Wrapper interface
class WrapperInterface:
    library_version = "3.6.1"       # The library version that wrapper is based on
    default_direction = "minimize"  # Default direction

    def __init__(self, objective, search_space):
        self.__objective = objective
        self.__search_space = search_space

    # Normalize parameters
    def _wrap_normalize_parameters(self, trial, search_space):
        # Get params
        params = [trial.suggest_float(name, low, high) for name, (low, high) in search_space.items()]
        # normalize params
        normalized_params = {name: param_value for name, param_value in zip(search_space.keys(), params)}
        # Return normalized params
        return normalized_params

    # Setup optimizer
    def _wrap_setup(self, objective):
        # Disable feedback from Optuna
        optuna.logging.disable_default_handler()
        optuna.logging.get_logger("optuna").addHandler(logging.NullHandler())

        self._study = optuna.create_study(direction="minimize", sampler=optuna.samplers.TPESampler())
    
    # Take one optimizer step
    def _wrap_step(self, objective):
        self._study.optimize(objective, n_trials=1)
        return self._study.best_params, self._study.best_value

    # Apply optimizer
    def __optimisation_loop(self, max_steps, target_value):
        step = 0
        while True:
            step += 1
            # Perform optimizer
            best_params, best_value = self._wrap_step()
            # Stop when target_value is reached
            if target_value:
                if best_params >= target_value:
                    break
            # Stop when max_steps is reached
            if max_steps:
                if step >= max_steps:
                    break
        return best_params, best_value

    def optimize(self, invert, max_steps=None, target_value=None):
        # Create the final objective function. Normilize parameters and set the direction.
        def final_objective(params):
            # Normalize parameters
            params = self._wrap_normalize_parameters(params, self.__search_space)
            result = self.__objective(params)
            # Invert result if needed
            return -result if invert else result
        
        # Setup optimizer
        self._wrap_setup(final_objective)

        # Run optimizer
        params, score = self.__optimisation_loop(final_objective, max_steps, target_value)
        
        # Invert final score if needed
        score = -score if invert else score
        return params, score
