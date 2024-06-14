# from hyperopt import hp

from ..._core.wrapper_interface import WrapperInterface


# Wrapper for Hyperopt with TPE
class HyperoptTPE(WrapperInterface):
    library_version = "0.2.5"      # The library version that wrapper is based on
    default_direction = "minimize" # Default optimization direction

    # Normalize parameters
    def _wrap_norm_parameters(self, params):
        return params  # No normalization needed for Hyperopt

    # Apply optimizer
    def _wrap_execute_optimization(self, objective):
        # space = {name: hp.uniform(name, low, high) for name, (low, high) in self.search_space.items()}

        def objective_wrapper(params):
            return self.objective(params)

        # trials = hp.Trials()
        # best = hp.fmin(fn=objective, space=space, algo=hp.tpe.suggest, max_evals=100, trials=trials)

        # best_trial = trials.best_trial
        # best_params = best_trial['misc']['vals']
        # best_params = {key[0]: value[0] for key, value in best_params.items()}
        # best_score = best_trial['result']['loss']
        best_params, best_score = (0, 0)
        return best_params, best_score
