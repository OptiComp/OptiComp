from dataclasses import dataclass

from bayes_opt import BayesianOptimization, UtilityFunction

from ..._core.wrapper_interface import WrapperInterface


# Wrapper interface
class Bayesian(WrapperInterface):
    def __init__(self, objective, search_space):
        super().__init__("1.4.3", "maximize", objective, search_space)

    @dataclass
    class Config:
        kappa: float = 2.5
        xi: float = 0.0

    def _wrap_normalize_parameters(self, params, search_space):
        # No need to normalize parameters for BayesianOptimization
        return params
    
    def _wrap_setup(self, objective, search_space):
        self._optimizer = BayesianOptimization(
            f=None,
            pbounds=search_space,
            random_state=42,
            verbose=False,
            allow_duplicate_points=True
        )
        
        self._utility = UtilityFunction(kind="ucb", kappa=self.Config.kappa, xi=self.Config.xi)

        next_point_to_probe = self._optimizer.suggest(self._utility)

        target = objective(next_point_to_probe)

        self._optimizer.register(
            params=next_point_to_probe,
            target=target
        )
            
    def _wrap_step(self, objective, search_space):
        next_point = self._optimizer.suggest(self._utility)
        target = objective(next_point)
        self._optimizer.register(params=next_point, target=target)
            
        best_params = self._optimizer.max['params']
        best_score = self._optimizer.max['target']

        return best_params, best_score
