from hyperopt import fmin, tpe, hp, Trials, STATUS_OK
from ...wrapper_interface import WrapperInterface


class HyperoptTPEWrapper(WrapperInterface):
    name = "HyperoptTPE"           # Name for the wrapper
    library_version = "0.2.7"      # The library version that wrapper is based on
    default_direction = "minimize" # Give default direction

    # Normalize parameters
    def norm_parameters(self):
        space = {name: hp.uniform(name, low, high) for name, (low, high) in self.search_space.items()}
        print(space)
        # Normilize params
        normalized_params = {}
        for name, param_value in zip(self.search_space.keys(), space):
            normalized_params[name] = param_value
        # Return normilized params
        return space

    # Apply optimizer
    def optimize(self, objective):
        # Define the search space
        space = self.norm_parameters()

        # Define the objective function for Hyperopt
        def hyperopt_objective(params):
            # Reformat params to match objective input
            formatted_params = {name: params[name] for name in self.search_space.keys()}
            return {'loss': objective(formatted_params), 'status': STATUS_OK}

        trials = Trials()
        best = fmin(
            fn=hyperopt_objective,
            space=space,
            algo=tpe.suggest,
            max_evals=100,
            trials=trials
        )
        best_loss = min([trial['result']['loss'] for trial in trials.trials])
        return best, best_loss