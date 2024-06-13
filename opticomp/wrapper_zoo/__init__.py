from typing import Callable


# ================================================================================ Optuna
def optuna_tpe(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .optuna.wrapper_optuna_tpe import OptunaTPE
    return OptunaTPE(objective, search_space)


def optuna_random(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .optuna.wrapper_optuna_random import OptunaRandom
    return OptunaRandom(objective, search_space)


def optuna_grid_search(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .optuna.wrapper_optuna_grid_search import OptunaGridSearch
    return OptunaGridSearch(objective, search_space)


# ================================================================================ Hyperopt
def hyperopt_tpe(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .hyperopt.wrapper_hyperopt_tpe import HyperoptTPE
    return HyperoptTPE(objective, search_space)


# ================================================================================ BayesianOpt
def bayesian(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .bayes_opt.wrapper_bayesian_optimization import Bayesian
    return Bayesian(objective, search_space)
