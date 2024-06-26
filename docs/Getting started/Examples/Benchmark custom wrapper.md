# Using BenchmarkSuite with a Custom Wrapper

This example demonstrates how to use the `BenchmarkSuite` to compare and optimize using multiple wrappers from the `wrapper_zoo`, including a custom wrapper. This example will create a wrapper for the optuna library.
For more information on how to create custom wrappers, please see [Custom Wrappers](Common%20wrappers.md).

```python
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
        self._study.optimize(objective, n_trials=1)
        return self._study.best_params, self._study.best_value

# Get common objective from objective_zoo
objective, search_space = objective_zoo.fetch_sphere_function()

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_tpe())
benchmark_suite.add_wrapper(wrapper_zoo.fetch_bayesian())
benchmark_suite.add_wrapper(CustomWrapper)

# Compare and optimize using the added wrappers
results = benchmark_suite.benchmark(direction="minimize", max_steps=100, target_score=200, verbose=True, progress_bar=True)
```

This script sets up a benchmarking environment with a common objective and search space, adds both common and custom wrappers, and then runs the optimization process to compare their performance.
