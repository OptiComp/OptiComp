# List of wrapper modules, class names, and optimizer names
wrapper_info = [
    ("opticomp.wrappers.optuna.wrapper_optuna_random", "OptunaRandomWrapper", "OptunaRandom"),
    ("opticomp.wrappers.optuna.wrapper_optuna_tpe", "OptunaTPEWrapper", "OptunaTPE"),
    ("opticomp.wrappers.optuna.wrapper_optuna_grid_search", "OptunaGridSearchWrapper", "OptunaGridSearch"),
    ("opticomp.wrappers.hyperopt.wrapper_hyperopt_tpe", "HyperoptTPEWrapper", "HyperoptTPE"),
    ("opticomp.wrappers.bayes_opt.wrapper_bayesian_optimization", "BayesianOptWrapper", "BayesianOpt"),
]