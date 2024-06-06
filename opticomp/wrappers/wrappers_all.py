# Imports
from .optuna.wrapper_optuna_random import OptunaRandomWrapper
from .optuna.wrapper_optuna_tpe import OptunaTPEWrapper

from .hyperopt.wrapper_hyperopt_tpe import HyperoptTPEWrapper

from .bayes_opt.wrapper_bayesian_optimization import BayesianOptWrapper

def get_wrappers():
    # Create wrappers list
    wrappers = []
    # ============================================== Optuna
    wrappers.append(OptunaRandomWrapper)
    wrappers.append(OptunaTPEWrapper)
    # ============================================== Hyperopt
    wrappers.append(HyperoptTPEWrapper)
    # ============================================== BayesianOptimization
    wrappers.append(BayesianOptWrapper)

    # Return all buildin wrappers
    return wrappers