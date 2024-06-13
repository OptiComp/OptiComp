Module opticomp.wrapper_zoo.wrapper_interface
=============================================

Classes
-------

`WrapperInterface(library_version: str, default_direction: str, objective: Callable[[dict[str, float]], float], search_space: dict[str, tuple[float, float]])`
:   Helper class that provides a standard way to create an ABC using
    inheritance.

    ### Ancestors (in MRO)

    * abc.ABC

    ### Descendants

    * opticomp.wrapper_zoo.bayes_opt.wrapper_bayesian_optimization.Bayesian
    * opticomp.wrapper_zoo.hyperopt.wrapper_hyperopt_tpe.HyperoptTPE
    * opticomp.wrapper_zoo.optuna.wrapper_optuna_grid_search.OptunaGridSearch
    * opticomp.wrapper_zoo.optuna.wrapper_optuna_random.OptunaRandom
    * opticomp.wrapper_zoo.optuna.wrapper_optuna_tpe.OptunaTPE

    ### Class variables

    `Config`
    :

    `default_direction: str`
    :

    `library_version: str`
    :

    ### Methods

    `initialize(self, objective: Callable[[dict[str, float]], float], search_space: dict[str, tuple[float, float]])`
    :   Initialize the wrapper with an objective function and search space.
        
        Parameters
        ----------
        objective : Callable[[dict[str, float]], float]
            The objective function to be optimized.
        search_space : dict[str, tuple[float, float]
            The search space defining the range of each parameter.

    `optimize(self, direction: str, max_steps: int = None, target_score: int = None, progress_bar: bool = False) ‑> tuple[dict[str, float], float, int]`
    :   Run the optimizer on the provided objective and search space.
        
        Parameters
        ----------
        direction : str
            The direction of optimization, either "minimize" or "maximize".
        max_steps : int, optional
            The maximum number of optimization steps. If not provided, target_score must be provided.
        target_score : int, optional
            The target score to achieve. If not provided, max_steps must be provided.
        progress_bar : bool, optional
            Show progress bar.
            This requires the tqdm library.
        
        Returns
        -------
        tuple
            A tuple containing the following elements:
            - dict[str, float]: The optimized parameters.
            - float: The resulting score.
            - int: The number of steps taken.