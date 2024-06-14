import logging

import optuna

from ..._core.wrapper_interface import WrapperInterface


class OptunaRandom(WrapperInterface):
    def __init__(self, objective, search_space):
        super().__init__("3.6.1", "minimize", objective, search_space)

    def _wrap_normalize_parameters(self, trial, search_space):
        params = [trial.suggest_float(name, low, high) for name, (low, high) in search_space.items()]
        normalized_params = {name: param_value for name, param_value in zip(search_space.keys(), params)}
        return normalized_params

    def _wrap_setup(self, objective, search_space):
        optuna.logging.disable_default_handler()
        optuna.logging.get_logger("optuna").addHandler(logging.NullHandler())

        self._study = optuna.create_study(direction="minimize", sampler=optuna.samplers.RandomSampler())
    
    def _wrap_step(self, objective, search_space):
        self._study.optimize(objective, n_trials=1)
        return self._study.best_params, self._study.best_value