from bayes_opt import BayesianOptimization, UtilityFunction

from ...wrapper_interface import WrapperInterface


# Wrapper interface
class BayesianOpt(WrapperInterface):
    library_version = "1.4.3"      # The library version that wrapper is based on
    default_direction = "maximize" # Default direction

    # Config class
    class Config:
        kappa = 2.5
        xi = 0.0

    # Normalize parameters
    def _wrap_normalize_parameters(self, params, search_space):
        # No need to normalize parameters for BayesianOptimization
        return params
    
    # Setup optimizer
    def _wrap_setup(self, objective, search_space):
        # Initialize BayesianOptimization object
        self._optimizer = BayesianOptimization(
            f=None,                   # Placeholder for objective function
            pbounds=search_space,     # Parameter bounds
            random_state=42,          # Random seed
            verbose=False             # Disable verbosity
        )
        
        # Initialize utility function (Upper Confidence Bound)
        self._utility = UtilityFunction(kind="ucb", kappa=self.Config.kappa, xi=self.Config.xi)

        # Get the next point to probe using the utility function
        next_point_to_probe = self._optimizer.suggest(self._utility)

        # Call the objective function with the suggested point
        target = objective(next_point_to_probe)

        # Register the result of the probe
        self._optimizer.register(
            params=next_point_to_probe,
            target=target
        )
            
    # Take one optimizer step
    def _wrap_step(self, objective, search_space):
        next_point = self._optimizer.suggest(self._utility)  # Get the next point to probe
        target = objective(next_point)          # Call the objective function with the suggested point
        self._optimizer.register(params=next_point, target=target)  # Register the result of the probe
            
        # Extract best parameters and best score
        best_params = self._optimizer.max['params']
        best_score = self._optimizer.max['target']

        # Return best score
        return best_params, best_score
