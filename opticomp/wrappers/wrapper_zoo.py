# List of wrapper modules, class names, and optimizer names
wrapper_info = [
    # Optuna
    ("opticomp.wrappers.optuna.wrapper_optuna_random", "OptunaRandom"),
    ("opticomp.wrappers.optuna.wrapper_optuna_tpe", "OptunaTPE"),
    ("opticomp.wrappers.optuna.wrapper_optuna_grid_search", "OptunaGridSearch"),
    # Hyperopt
    ("opticomp.wrappers.hyperopt.wrapper_hyperopt_tpe", "HyperoptTPE"),
    # Bayesian
    ("opticomp.wrappers.bayes_opt.wrapper_bayesian_optimization", "BayesianOpt"),
]


# ============================================================== Optuna
def optuna_tpe(objective, search_space):
    from .optuna.wrapper_optuna_tpe import OptunaTPE
    return OptunaTPE(objective, search_space)


def optuna_random(objective, search_space):
    from .optuna.wrapper_optuna_random import OptunaRandom
    return OptunaRandom(objective, search_space)


def optuna_grid_search(objective, search_space):
    from .optuna.wrapper_optuna_grid_search import OptunaGridSearch
    return OptunaGridSearch(objective, search_space)


# ============================================================== Hyperopt
def hyperopt_tpe(objective, search_space):
    from .hyperopt.wrapper_hyperopt_tpe import HyperoptTPE
    return HyperoptTPE(objective, search_space)


# ============================================================== BayesianOpt
def bayesian(objective, search_space):
    from .bayes_opt.wrapper_bayesian_optimization import BayesianOpt
    return BayesianOpt(objective, search_space)