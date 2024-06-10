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