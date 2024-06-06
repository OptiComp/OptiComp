# Imports
from .optuna.wrapper_optuna_random import OptunaRandomWrapper
from .optuna.wrapper_optuna_tpe import OptunaTPEWrapper

def get_wrappers():
    # Return all buildin wrappers
    return [OptunaRandomWrapper, OptunaTPEWrapper]