# Imports
from .optuna.wrapper_optuna_random import OptunaRandomWrapper
from .optuna.wrapper_optuna_tpe import OptunaTPEWrapper

from .hyperopt.wrapper_hyperopt_tpe import HyperoptTPEWrapper

def get_wrappers():
    # Create wrappers list
    wrappers = []
    # ============================================== Optuna
    wrappers.append(OptunaRandomWrapper)
    wrappers.append(OptunaTPEWrapper)
    # ============================================== Hyperopt
    wrappers.append(HyperoptTPEWrapper)

    # Return all buildin wrappers
    return wrappers