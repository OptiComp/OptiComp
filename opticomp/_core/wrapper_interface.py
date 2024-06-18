import time
import warnings
from abc import ABC
from dataclasses import dataclass
from typing import Callable

import psutil

from .result_wrapper import WrapperResults


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
        score_history = []
        best_score = None
        best_params = None
        steps = 0

        cpu_history = []
        ram_history = []
        process = psutil.Process()

        while True:
            steps += 1

            params, score = self._wrap_step(final_objective, search_space)
            cpu_history.append(process.cpu_percent(interval=None) / psutil.cpu_count()) # Normalize by dividing by the number of cores)
            ram_history.append(process.memory_info().rss / 1024 ** 2)  # Convert to MB

            # Invert best_score back to normal, if invert == True (see 'final_objective' in 'optimize' below)
            norm_score = -score if invert else score
            score_history.append(norm_score)

            if pbar:
                pbar.update(1)

            if not best_score:
                best_score = score
                best_params = params
            elif score > best_score and direction == "maximize":
                best_score = score
                best_params = params
            elif score < best_score and direction == "minimize":
                best_score = score
                best_params = params

            if max_steps:
                if steps >= max_steps:
                    break
            if target_score:
                if norm_score >= target_score and direction == "maximize":
                    break
                elif norm_score <= target_score and direction == "minimize":
                    break

        return best_params, best_score, steps, score_history, cpu_history, ram_history
    
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
        WrapperResults
            A class containing the wrapper's results
        """
        if not max_steps and not target_score:
            raise ValueError("Either max_steps or target_score must be provided")
        if self.__objective is None or self.__search_space is None:
            raise ValueError("Wrapper not initialized. Please use 'wrapper.initialize(objective, search_space)'.")
        if direction not in {'minimize', 'maximize'}:
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
        best_params, best_score, steps, score_history, cpu_history, ram_history = self.__optimization_loop(final_objective, self.__search_space, max_steps, target_score, direction, invert, progress_bar)
        elapsed_time = time.time() - start_time
        
        # Invert score back to normal, if invert == True (see 'final_objective' above)
        best_score = -best_score if invert else best_score
        return WrapperResults(self.__class__.__name__,
                            best_params,
                            best_score,
                            score_history,
                            elapsed_time,
                            steps,
                            cpu_history,
                            ram_history)
    
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
