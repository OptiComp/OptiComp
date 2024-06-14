import time
import warnings
from abc import ABC
from dataclasses import dataclass
from typing import Callable

from .result_wrapper import WrapperResult


class WrapperInterface(ABC):
    library_version: str
    default_direction: str

    __objective: Callable[[dict[str, float]], float]
    __search_space: dict[str, tuple[float, float]]
    
    @dataclass
    class Config:
        empty: None

    def __init__(self, library_version: str, default_direction: str, objective: Callable[[dict[str, float]], float], search_space: dict[str, tuple[float, float]]):
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
    def __optimization_loop(self, final_objective, search_space, max_steps, target_score, direction, invert, progress_bar):
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
            best_params, best_score = self._wrap_step(final_objective, search_space)
            if pbar:
                pbar.update(1)
            if max_steps:
                if steps >= max_steps:
                    break
            if target_score:
                # Invert best_score back to normal, if invert == True (see 'final_objective' in 'optimize' below)
                norm_score = -best_score if invert else best_score
                if norm_score >= target_score and direction == "maximize":
                    break
                elif norm_score <= target_score and direction == "minimize":
                    break
        return best_params, best_score, steps
    
    # Run optimizer
    def optimize(self, direction: str, max_steps: int = None, target_score: float = None, progress_bar: bool = False):
        """
        Run the optimizer on the provided objective and search space.

        Parameters
        ----------
        direction : str
            The direction of optimization, either "minimize" or "maximize".
        max_steps : int, optional
            The maximum number of optimization steps. If not provided, target_score must be provided.
        target_score : float, optional
            The target score to achieve. If not provided, max_steps must be provided.
        progress_bar : bool, optional
            Show progress bar.
            This requires the tqdm library.

        Returns
        -------
        WrapperResult
            A class containing the wrapper's results
        """
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        if self.__objective is None or self.__search_space is None:
            raise ValueError("Wrapper not initialized. Please use 'wrapper.initialize(objective, search_space)'.")
        if direction != 'minimize' and direction != 'maximize':
            raise ValueError(f"Unknown direction: '{direction}'. Please choose 'minimize' or 'maximize'.")
        
        invert = False
        if self.default_direction != direction:
            invert = True
        
        # Create the final objective function. Normilize parameters and set the direction.
        def final_objective(params):
            params = self._wrap_normalize_parameters(params, self.__search_space)
            score = self.__objective(params)
            # Invert score to set optimizer direction, if invert == True
            return -score if invert else score
        
        self._wrap_setup(final_objective, self.__search_space)
        
        start_time = time.time()
        params, score, steps = self.__optimization_loop(final_objective, self.__search_space, max_steps, target_score, direction, invert, progress_bar)
        elapsed_time = time.time() - start_time
        
        # Invert score back to normal, if invert == True (see 'final_objective' above)
        score = -score if invert else score
        return WrapperResult(self.__class__.__name__,
                            params,
                            score,
                            elapsed_time,
                            steps)
    
    def initialize(self, objective: Callable[[dict[str, float]], float], search_space: dict[str, tuple[float, float]]):
        """
        Initialize the wrapper with an objective function and search space.

        Parameters
        ----------
        objective : Callable[[dict[str, float]], float]
            The objective function to be optimized.
        search_space : dict[str, tuple[float, float]
            The search space defining the range of each parameter.
        """
        self.__objective = objective
        self.__search_space = search_space
