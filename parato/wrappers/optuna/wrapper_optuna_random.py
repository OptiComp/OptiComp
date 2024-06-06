# Imports
import optuna
from parato.wrapper_interface import WrapperInterface

class OptunaTPEWrapper(WrapperInterface):
    name = "OptunaTPE"  # Name for the wrapper

    def optimize(self):
        def optuna_objective(trial):
            params = [trial.suggest_uniform(name, low, high) for name, (low, high) in self.search_space.items()]
            return self.objective(params)
        
        study = optuna.create_study(direction='minimize', sampler=optuna.samplers.RandomSampler())
        study.optimize(optuna_objective, n_trials=100)
        return study.best_params, study.best_value