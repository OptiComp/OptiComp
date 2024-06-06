# Imports
from .optuna.wrapper_optuna_random import OptunaRandomWrapper
from .optuna.wrapper_optuna_tpe import OptunaTPEWrapper

def get_wrappers():
    # Create wrappers list
    wrappers = []
    # ============================================== Optuna
    wrappers.append(OptunaRandomWrapper)
    wrappers.append(OptunaTPEWrapper)

    # Return all buildin wrappers
    return wrappers