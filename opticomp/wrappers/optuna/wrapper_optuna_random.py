# Imports
import optuna
import logging
from ...wrapper_interface import WrapperInterface

    
class OptunaRandomWrapper(WrapperInterface):
    name = "OptunaRandom"           # Name for the wrapper
    library_version = "3.6.1"       # The library version that wrapper is based on
    default_direction = "minimize"  # Default direction

    # Normalize parameters
    def _wrap_norm_parameters(self, trial):
        # Get params
        params = [trial.suggest_float(name, low, high) for name, (low, high) in self.search_space.items()]
        # Normilize params
        normalized_params = {name: param_value for name, param_value in zip(self.search_space.keys(), params)}
        # Return normilized params
        return normalized_params

    # Apply optimizer
    def _wrap_execute_optimization(self, objective, n_steps):
        # Disable feedback from Optuna
        optuna.logging.disable_default_handler()
        optuna.logging.get_logger("optuna").addHandler(logging.NullHandler())

        study = optuna.create_study(direction="minimize", sampler=optuna.samplers.TPESampler())
        study.optimize(objective, n_trials=n_steps)
        return study.best_params, study.best_value