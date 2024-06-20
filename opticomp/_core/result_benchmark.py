import os
from operator import attrgetter

import matplotlib.pyplot as plt

from .result_wrapper import WrapperResults


class BenchmarkResults():
    def __init__(self):
        self.results_all: dict[str, list[WrapperResults]] = {}
        self._measure_method: str = "median"

    def _add_result(self, wrapper_result):
        optimizer_name = wrapper_result[0].name
        if optimizer_name not in self.results_all:
            self.results_all[optimizer_name] = []
        self.results_all[optimizer_name].extend(wrapper_result)

    def _normalize_name(self, name):
        norm_name = name.lower().replace(" ", "").replace("_", "").replace("-", "")
        return norm_name
    
    # ============================================================== Measure results

    def set_measure(self, measure: str = "median"):
        """
        Set the current measure for summarizing results.

        Parameters
        ----------
        measure : str
            The measure to use ("median", "max", "min"). Default is "median".
        """
        self.measure = measure.lower()

    def _median(self, results):
        # Get the median result, based on score.
        sorted_results = sorted(results, key=attrgetter('best_score'))
        median_index = len(sorted_results) // 2
        return results[median_index]
    
    def _max(self, results):
        # Get the result with the highest score.
        return max(results, key=attrgetter('best_score'))
    
    def _min(self, results):
        # Get the result with the lowest score.
        return max(results, key=attrgetter('best_score'))

    def _apply_measure_results(self, results):
        if self._measure_method == "median":
            measure_result = self._median(results)
        elif self._measure_method == "max":
            measure_result = self._max(results)
        elif self._measure_method == "min":
            measure_result = self._min(results)
        else:
            raise ValueError(f"Measure '{self._measure_method}' not recognized.")
        return measure_result

    # ============================================================== Public methods

    def summarize(self, wrapper_name: str):
        """
        Summarize the results for a specific wrapper.
        
        Parameters
        ----------
        wrapper_name : str
            Provide the wrapper name you want to summarize.
        """
        for results_name in self.results_all:
            results_opt = self.results_all[results_name]
            result = self._apply_measure_results(results_opt)
            if result.name.lower() == self._normalize_name(wrapper_name):
                result.summarize()
                return
        print(f"No results found for optimizer: {wrapper_name}")

    def summarize_all(self):
        """
        Summarize the results for all wrappers.
        """
        for results_name in self.results_all:
            results_opt = self.results_all[results_name]
            result = self._apply_measure_results(results_opt)
            result.summarize()

    def plot_score(self, wrapper_names: list[str] = None, show: bool = False, save_dir: str = None):
        """
        Plot one graph to visualize all the wrapper histories.
        
        Parameters
        ----------
        wrapper_names: list[str] = None, optional
            Give a list of which wrappers you want to plot. The other wrappers will be excluded.
        show : bool = False, optional
            Set to true to show the graph.
        save_dir: str = None. optional
            Give a dir to save the graph to.
        """
        if wrapper_names:
            norm_wrapper_names = [self._normalize_name(name) for name in wrapper_names]

        plt.figure()

        for results_name in self.results_all:
            results_opt = self.results_all[results_name]
            result = self._apply_measure_results(results_opt)
            if wrapper_names and result.name.lower() not in norm_wrapper_names:
                continue
            x = []
            y = result.score_history
            for step in range(len(result.score_history)):
                x.append(step + 1)
            plt.plot(x, y, label=result.name)

        plt.title("Summary")
        plt.xlabel('Steps')
        plt.ylabel('Score')
        plt.legend()

        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
            file_path = os.path.join(save_dir, "plot_summary.png")
            plt.savefig(file_path)
        if show:
            plt.show()

    def fetch_wrapper_result(self, wrapper_name: str) -> WrapperResults:
        """
        Fetch and return the result class of a specific wrapper
        
        Parameters
        ----------
        wrapper_name : str
            Provide the wrapper name you want to fetch.

        Returns
        -------
        class WrapperResults
            A class containing the results for a specific wrapper
        """
        for results_name in self.results_all:
            print(results_name)
            results_opt = self.results_all[results_name]
            print(self.results_all)
            print(results_opt)
            result = self._apply_measure_results(results_opt)
            if result.name.lower() == self._normalize_name(wrapper_name):
                return result
        print(f"No results found for wrapper: {wrapper_name}")
        # Create and return an empty WrapperResults so the autocomplete always works
        return WrapperResults("EmptyResult")
