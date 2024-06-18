import logging

import optuna

from opticomp import BenchmarkSuite, WrapperInterface, objective_zoo, wrapper_zoo


# Create a custom wrapper
class CustomWrapper(WrapperInterface):
    def __init__(self, objective, search_space):
        # Give library version and default optimizer direction
        super().__init__("3.6.1", "minimize", objective, search_space)

    # Normalize the output parameters of the optimizer to work with the BenchmarkSuite
    def _wrap_normalize_parameters(self, trial, search_space):
        params = [trial.suggest_float(name, low, high) for name, (low, high) in search_space.items()]
        normalized_params = {name: param_value for name, param_value in zip(search_space.keys(), params)}
        return normalized_params

    # Setup optimizer
    def _wrap_setup(self, objective, search_space):
        optuna.logging.disable_default_handler()
        optuna.logging.get_logger("optuna").addHandler(logging.NullHandler())
        self._study = optuna.create_study(direction="minimize", sampler=optuna.samplers.RandomSampler())
    
    # Take ONE optimizer step. never more than one
    def _wrap_step(self, objective, search_space):
        trial = self._study.ask()
        result = objective(trial)
        self._study.tell(trial, result)
        return trial.params, result

# Get common objective from objective_zoo
objective, search_space = objective_zoo.fetch_sphere_function()

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Create an instance of the custom wrapper
custom_wrapper = CustomWrapper(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_tpe())
benchmark_suite.add_wrapper(wrapper_zoo.fetch_bayesian())
benchmark_suite.add_wrapper(custom_wrapper)

# Compare and optimize using the added wrappers
results = benchmark_suite.benchmark(direction="minimize", max_steps=100, target_score=200, verbose=True, progress_bar=True)
