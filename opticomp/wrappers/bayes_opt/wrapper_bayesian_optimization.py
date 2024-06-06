from bayes_opt import BayesianOptimization
from ...wrapper_interface import WrapperInterface


# Wrapper interface
class BayesianOptWrapper(WrapperInterface):
    name = "BayesianOpt"           # Name for the wrapper
    library_version = "1.4.3"      # The library version that wrapper is based on
    default_direction = "maximize" # Give default direction

    def norm_parameters(self, params):
        # No need to normalize parameters for BayesianOptimization
        return params
    
    def optimize(self, objective):
        optimizer = BayesianOptimization(
            f=lambda **params: objective(params),  # Modified to accept **params
            pbounds=self.search_space,
            random_state=42  # You can set a random state for reproducibility
        )

        optimizer.maximize(init_points=5, n_iter=100)

        # Extract best parameters and best score
        best_params = optimizer.max['params']
        best_score = optimizer.max['target']

        return best_params, best_score

    