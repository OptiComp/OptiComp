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
