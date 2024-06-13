Module opticomp.wrapper_zoo
===========================

Sub-modules
-----------
* opticomp.wrapper_zoo.bayes_opt
* opticomp.wrapper_zoo.hyperopt
* opticomp.wrapper_zoo.optuna
* opticomp.wrapper_zoo.wrapper_interface

Functions
---------

    
`fetch_bayesian(objective: Callable[[dict[str, float]], float] = None, search_space: dict[str, tuple[float, float]] = None)`
:   Fetch optimizer wrapper from wrapper zoo.
    
    Optionally pass parameters to initialize the wrapper.

    
`fetch_hyperopt_tpe(objective: Callable[[dict[str, float]], float] = None, search_space: dict[str, tuple[float, float]] = None)`
:   Fetch optimizer wrapper from wrapper zoo.
    
    Optionally pass parameters to initialize the wrapper.

    
`fetch_optuna_grid_search(objective: Callable[[dict[str, float]], float] = None, search_space: dict[str, tuple[float, float]] = None)`
:   Fetch optimizer wrapper from wrapper zoo.
    
    Optionally pass parameters to initialize the wrapper.

    
`fetch_optuna_random(objective: Callable[[dict[str, float]], float] = None, search_space: dict[str, tuple[float, float]] = None)`
:   Fetch optimizer wrapper from wrapper zoo.
    
    Optionally pass parameters to initialize the wrapper.

    
`fetch_optuna_tpe(objective: Callable[[dict[str, float]], float] = None, search_space: dict[str, tuple[float, float]] = None)`
:   Fetch optimizer wrapper from wrapper zoo.
    
    Optionally pass parameters to initialize the wrapper.