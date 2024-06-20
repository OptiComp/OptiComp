import logging

from hyperopt import Trials, fmin, tpe

from ..._core.wrapper_interface import WrapperInterface


class HyperoptTPE(WrapperInterface):
    def __init__(self, objective, search_space):
        super().__init__("1.0", "minimize", objective, search_space)
        self._trials = Trials()

    def _wrap_normalize_parameters(self, trial, search_space):
        normalized_params = {name: trial[name] for name in search_space.keys()}
        return normalized_params

    def _wrap_setup(self, objective, search_space):
        logging.getLogger('hyperopt').setLevel(logging.WARNING)

    def _wrap_step(self, objective, search_space):
        best = fmin(objective, search_space, algo=tpe.suggest, max_evals=len(self._trials) + 1, trials=self._trials, show_progressbar=False)
        return best, self._trials.best_trial['result']['loss']
