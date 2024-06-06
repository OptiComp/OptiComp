# Imports
import optuna
import logging
from ...wrapper_interface import WrapperInterface

    
class OptunaRandomWrapper(WrapperInterface):
    name = "OptunaRandom"           # Name for the wrapper
    library_version = "3.6.1"       # The library version that wrapper is based on
    default_direction = "minimize"  # Give default direction

    # Normalize parameters
    def norm_objective(self, trial):
        params = [trial.suggest_float(name, low, high) for name, (low, high) in self.search_space.items()]
        return self.objective(params)

    def optimize(self, invert_direction):
        # Disable feedback from Optuna
        optuna.logging.disable_default_handler()
        optuna.logging.get_logger("optuna").addHandler(logging.NullHandler())

        # Invert direction if required
        direction = "maximize" if invert_direction else self.default_direction
        
        study = optuna.create_study(direction=direction, sampler=optuna.samplers.TPESampler())
        study.optimize(self.norm_objective, n_trials=100)
        return study.best_params, study.best_value