# Imports
from parato.wrappers.optuna.wrapper_optuna_random import OptunaRandomWrapper
from parato.wrappers.optuna.wrapper_optuna_tpe import OptunaTPEWrapper

def get_wrappers():
    # Return all buildin wrappers
    return [OptunaRandomWrapper, OptunaTPEWrapper]