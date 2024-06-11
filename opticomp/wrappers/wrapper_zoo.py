from typing import Callable


# ============================================================== Optuna
def optuna_tpe(objective: Callable[[list[int]], int], search_space: dict[str, tuple[int, int]]):
    from .optuna.wrapper_optuna_tpe import OptunaTPE
    return OptunaTPE(objective, search_space)


def optuna_random(objective: Callable[[list[int]], int], search_space: dict[str, tuple[int, int]]):
    from .optuna.wrapper_optuna_random import OptunaRandom
    return OptunaRandom(objective, search_space)


def optuna_grid_search(objective: Callable[[list[int]], int], search_space: dict[str, tuple[int, int]]):
    from .optuna.wrapper_optuna_grid_search import OptunaGridSearch
    return OptunaGridSearch(objective, search_space)


# ============================================================== Hyperopt
def hyperopt_tpe(objective: Callable[[list[int]], int], search_space: dict[str, tuple[int, int]]):
    from .hyperopt.wrapper_hyperopt_tpe import HyperoptTPE
    return HyperoptTPE(objective, search_space)


# ============================================================== BayesianOpt
def bayesian(objective: Callable[[list[int]], int], search_space: dict[str, tuple[int, int]]):
    from .bayes_opt.wrapper_bayesian_optimization import BayesianOpt
    return BayesianOpt(objective, search_space)



    