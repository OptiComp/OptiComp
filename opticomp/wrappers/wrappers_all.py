# Imports
from .optuna.wrapper_optuna_random import OptunaRandomWrapper
from .optuna.wrapper_optuna_tpe import OptunaTPEWrapper

from .hyperopt.wrapper_hyperopt_tpe import HyperoptTPEWrapper

from .bayes_opt.wrapper_bayesian_optimization import BayesianOptimization

def get_wrappers():
    # Create wrappers list
    wrappers = []
    # ============================================== Optuna
    wrappers.append(OptunaRandomWrapper)
    wrappers.append(OptunaTPEWrapper)
    # ============================================== Hyperopt
    wrappers.append(HyperoptTPEWrapper)
    # ============================================== BayesianOptimization
    wrappers.append(BayesianOptimization)

    # Return all buildin wrappers
    return wrappers