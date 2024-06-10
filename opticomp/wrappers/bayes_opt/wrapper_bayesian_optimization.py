# Imports
from bayes_opt import BayesianOptimization, UtilityFunction

from ...wrapper_interface import WrapperInterface


# Wrapper interface
class BayesianOpt(WrapperInterface):
    name = "BayesianOpt"           # Name for the wrapper
    library_version = "1.4.3"      # The library version that wrapper is based on
    default_direction = "maximize" # Default direction

    # Config class
    class Config:
        kappa = 2.5
        xi = 0.0

    def _wrap_norm_parameters(self, params):
        # No need to normalize parameters for BayesianOptimization
        return params
    
    def _wrap_execute_optimization(self, objective, n_steps):
        # Initialize BayesianOptimization object
        optimizer = BayesianOptimization(
            f=None,                   # Placeholder for objective function
            pbounds=self.search_space,  # Parameter bounds
            random_state=42,          # Random seed
            verbose=False             # Disable verbosity
        )
        
        # Initialize utility function (Upper Confidence Bound)
        utility = UtilityFunction(kind="ucb", kappa=self.Config.kappa, xi=self.Config.xi)

        # Get the next point to probe using the utility function
        next_point_to_probe = optimizer.suggest(utility)

        # Call the objective function with the suggested point
        target = objective(next_point_to_probe)

        # Register the result of the probe
        optimizer.register(
            params=next_point_to_probe,
            target=target
        )

        # Perform additional probes
        for _ in range(int(n_steps / 20)):
            next_point = optimizer.suggest(utility)  # Get the next point to probe
            target = objective(next_point)          # Call the objective function with the suggested point
            optimizer.register(params=next_point, target=target)  # Register the result of the probe
            

        # Extract best parameters and best score
        best_params = optimizer.max['params']
        best_score = optimizer.max['target']

        return best_params, best_score
    