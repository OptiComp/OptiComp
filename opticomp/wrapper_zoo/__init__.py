from typing import Callable


# ================================================================================ Optuna
def fetch_optuna_tpe(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .optuna.wrapper_optuna_tpe import OptunaTPE
    return OptunaTPE(objective, search_space)


def fetch_optuna_random(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .optuna.wrapper_optuna_random import OptunaRandom
    return OptunaRandom(objective, search_space)


# ================================================================================ BayesianOpt
def fetch_bayesian(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .bayes_opt.wrapper_bayesian_optimization import Bayesian
    return Bayesian(objective, search_space)


# ================================================================================ Sklearn
def fetch_sklearn_gridsearch(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .sklearn.wrapper_sklearn_gridsearch import SklearnGridSearch
    return SklearnGridSearch(objective, search_space)


# ================================================================================ Deap
def fetch_deap_ea(objective: Callable[[dict[str, float]], float] = None,
            search_space: dict[str, tuple[float, float]] = None):
    """ Fetch optimizer wrapper from wrapper zoo.\n
        Optionally pass parameters to initialize the wrapper."""
    from .deap.wrapper_deap_ea import DeapEA
    return DeapEA(objective, search_space)
