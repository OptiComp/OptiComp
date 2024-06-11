import logging

import optuna

from ...wrapper_interface import WrapperInterface


class OptunaTPE(WrapperInterface):
    library_version = "3.6.1"       # The library version that wrapper is based on
    default_direction = "minimize"  # Default direction

    # Normalize parameters
    def _wrap_normalize_parameters(self, trial, search_space):
        # Get params
        params = [trial.suggest_float(name, low, high) for name, (low, high) in search_space.items()]
        # Normilize params
        normalized_params = {name: param_value for name, param_value in zip(search_space.keys(), params)}
        # Return normilized params
        return normalized_params

    # Setup optimizer
    def _wrap_setup(self, objective, search_space):
        # Disable feedback from Optuna
        optuna.logging.disable_default_handler()
        optuna.logging.get_logger("optuna").addHandler(logging.NullHandler())

        self._study = optuna.create_study(direction="minimize", sampler=optuna.samplers.TPESampler())
    
    # Take one optimizer step
    def _wrap_step(self, objective, search_space):
        self._study.optimize(objective, n_trials=1)
        return self._study.best_params, self._study.best_value
    