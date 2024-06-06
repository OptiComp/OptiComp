# Imports
import optuna
import logging
from ...wrapper_interface import WrapperInterface


class OptunaTPEWrapper(WrapperInterface):
    name = "OptunaTPE"  # Name for the wrapper
    default_direction = "minimize" # Give default direction

    def optimize(self, invert_direction):
        # Disable feedback from Optuna
        optuna.logging.disable_default_handler()
        optuna.logging.get_logger("optuna").addHandler(logging.NullHandler())

        # Normalize parameters
        def optuna_objective(trial):
            params = [trial.suggest_float(name, low, high) for name, (low, high) in self.search_space.items()]
            return self.objective(params)
        
        # Invert direction if required
        direction = "maximize" if invert_direction else self.default_direction
        
        study = optuna.create_study(direction=direction, sampler=optuna.samplers.RandomSampler())
        study.optimize(optuna_objective, n_trials=100)
        return study.best_params, study.best_value
    