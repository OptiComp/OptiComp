import warnings
from abc import ABC
from typing import Callable


class WrapperInterface(ABC):
    library_version: str
    default_direction: str

    __objective: Callable[[list[int]], int]
    __search_space: dict[str, tuple[int, int]]
    
    config = {}

    def __init__(self, library_version: str, default_direction: str, objective: Callable[[list[int]], int], search_space: dict[str, tuple[int, int]]):
        self.library_version = library_version
        self.default_direction = default_direction
        self.__objective = objective
        self.__search_space = search_space
    
    # Normalize parameters
    def _wrap_normalize_parameters(self, params, search_space):
        raise NotImplementedError("The wrapper method '_wrap_normalize_parameters' should be overridden")
    
    # Setup optimizer
    def _wrap_setup(self, objective, search_space):
        raise NotImplementedError("The wrapper method '_wrap_setup' should be overridden")
    
    # Take one optimizer step
    def _wrap_step(self, objective, search_space):
        raise NotImplementedError("The wrapper method '_wrap_step' should be overridden")
    
    # Apply optimizer
    def __optimization_loop(self, final_objective, search_space, max_steps, target_score, direction, progress_bar):
        if progress_bar:
            try:
                from tqdm import tqdm
                pbar = tqdm(total=max_steps, desc="Benchmarking", unit="step", ascii=True, colour='green')
            except ImportError:
                pbar = None
                warnings.warn("The 'tqdm' library is required to utilize the progress bar. Please install it using 'pip install tqdm'.\n"
                                "Continuing without progress bar")
        else:
            pbar = None
        steps = 0
        while True:
            steps += 1
            best_params, best_value = self._wrap_step(final_objective, search_space)
            if pbar:
                pbar.update(1)
            if max_steps:
                if steps >= max_steps:
                    break
            if target_score:
                if abs(best_value) >= target_score and direction == "maximize":
                    break
                elif abs(best_value) <= target_score and direction == "minimize":
                    break
        return best_params, best_value, steps
    
    # Run optimizer
    def optimize(self, direction: str, max_steps: int = None, target_score: int = None, progress_bar: bool = False):
        """
        Run the optimizer on the provided objective and search space.

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
            - list[int]: The optimized parameters.
            - int: The resulting score.
            - int: The number of steps taken.
        """
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        
        invert = False
        if self.default_direction != direction:
            invert = True
        
        # Create the final objective function. Normilize parameters and set the direction.
        def final_objective(params):
            params = self._wrap_normalize_parameters(params, self.__search_space)
            result = self.__objective(params)
            return -result if invert else result
        
        self._wrap_setup(final_objective, self.__search_space)

        params, score, steps = self.__optimization_loop(final_objective, self.__search_space, max_steps, target_score, direction, progress_bar)
        
        score = -score if invert else score
        return params, score, steps
    
    def reinitialize(self, objective: Callable[[list[int]], int], search_space: dict[str, int]):
        """
        Reinitialize the wrapper with a new objective function and search space.

        Parameters
        ----------
        objective : Callable[[list[int]], int]
            The new objective function to be optimized.
        search_space : dict[str, int]
            The new search space defining the range of each parameter.
        """
        self.__objective = objective
        self.__search_space = search_space
    