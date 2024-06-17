import os

import matplotlib.pyplot as plt

from .result_wrapper import WrapperResults


class BenchmarkResults():
    def __init__(self):
        self.results = []

    def _add_result(self, wrapper_result):
        self.results.append(wrapper_result)

    def _normalize_name(self, name):
        norm_name = name.lower().replace(" ", "").replace("_", "").replace("-", "")
        return norm_name

    def summarize(self, wrapper_name: str):
        """
        Summarize the results for a specific wrapper.
        
        Parameters
        ----------
        wrapper_name : str
            Provide the wrapper name you want to summarize.
        """
        for result in self.results:
            if result.name.lower() == self._normalize_name(wrapper_name):
                result.summarize()
                return
        print(f"No results found for optimizer: {wrapper_name}")

    def summarize_all(self):
        """
        Summarize the results for all wrappers.
        """
        for result in self.results:
            result.summarize()

    def plot(self, wrapper_names: list[str] = None, show: bool = False, save_dir: str = None):
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

        for result in self.results:
            if wrapper_names and result.name.lower() not in norm_wrapper_names:
                continue
            x = []
            y = result.history
            for step in range(len(result.history)):
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
        for result in self.results:
            if result.name.lower() == self._normalize_name(wrapper_name):
                return result
        print(f"No results found for wrapper: {wrapper_name}")
        # Create and return an empty WrapperResults so the autocomplete always works
        return WrapperResults("EmptyResult", None, None, None, None)
