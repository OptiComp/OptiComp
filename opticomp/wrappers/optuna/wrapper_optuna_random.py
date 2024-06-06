# Imports
import optuna
import logging
from ...wrapper_interface import WrapperInterface

    
class OptunaRandomWrapper(WrapperInterface):
    name = "OptunaRandom"  # Name for the wrapper

    def optimize(self):
        # Disable feedback from Optuna
        optuna.logging.disable_default_handler()
        optuna.logging.get_logger("optuna").addHandler(logging.NullHandler())

        def optuna_objective(trial):
            params = [trial.suggest_float(name, low, high) for name, (low, high) in self.search_space.items()]
            return self.objective(params)
        
        study = optuna.create_study(direction='minimize', sampler=optuna.samplers.TPESampler())
        study.optimize(optuna_objective, n_trials=100)
        return study.best_params, study.best_value