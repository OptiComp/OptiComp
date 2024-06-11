# OptiComp
## Overview
OptiComp is a versatile optimization library designed to streamline the comparison of optimizers. With a straightforward approach, it facilitates the assessment of various optimizers by providing standard benchmark objectives. Whether utilizing built-in benchmarks or custom objectives, OptiComp empowers users to identify the most suitable optimizer for their specific goals. The library offers convenient wrappers for comparing optimizer libraries or enables users to create their own wrappers as needed. Simplifying the process, OptiComp empowers users to easily compare optimizers and determine the best fit for their optimization tasks.
<br>

## Features
- **Unified API:** Standardize different optimization libraries or custom optimizers with common wrappers.
- **Standard Wrappers:** Ready-to-use wrappers for popular optimization libraries like Optuna, bayes_opt, and Hyperopt.
- **Custom Wrappers:** Create your own wrappers for other libraries or your custom optimizers.
- **Standard Objectives:** Pick a standard objective to evaluate the optimizer on, providing predefined metrics for easier evaluation and comparison across different optimization algorithms.
- **Custom Objectives:** Create custom objectives to evaluate the optimizer on, allowing for tailored evaluation metrics based on specific tasks or requirements.
- **Optimizer Comparison:** Compare different wrappers on your objective to find the most effective optimizer.
- **Best Optimizer Selection:** Select the best wrapper for your objective with less computational overhead.
- **Direct Optimization:** Run optimizations directly using the provided wrappers.
<br>

## Installation
**Install OptiComp via pip:**

```
pip install opticomp
```
<br>

## Usage
**Benchmark Common Wrappers And Objectives:**
<br>Use the OptiComp common wrappers and objectives:
```python
from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# Get common objective from objective_zoo
objective, search_space = objective_zoo.sphere_function()

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.optuna_random(objective, search_space))
benchmark_suite.add_wrapper(wrapper_zoo.optuna_tpe(objective, search_space))
benchmark_suite.add_wrapper(wrapper_zoo.bayesian(objective, search_space))

# Compare and optimize using the added wrappers
best_result, all_results = benchmark_suite.benchmark(direction="minimize", max_steps=100, target_score=200, verbose=True)
```
<br>

**Custom Objective:**
<br>Create a custom objective and search_space:

```python
from opticomp import BenchmarkSuite, wrapper_zoo

# Custom objective
def objective(params):
    # Split params
    param1 = params['param1']
    param2 = params['param1']
    
    # Evaluate and calculate score
    score = param1 + param2

    # Return score
    return score

# Custom search_space
search_space = {'param1': (-100, 100),
                'param2': (-100, 100)}

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.optuna_random(objective, search_space))
benchmark_suite.add_wrapper(wrapper_zoo.optuna_tpe(objective, search_space))
benchmark_suite.add_wrapper(wrapper_zoo.bayesian(objective, search_space))

# Compare and optimize using the added wrappers
best_result, all_results = benchmark_suite.benchmark(direction="maximize", max_steps=100, target_score=190, verbose=True)
```
<br>

**Custom Wrapper:**
<br>Create a custom wrapper for any optimizer:
```python
import logging

import optuna

from opticomp import WrapperInterface, objective_zoo

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
objective, search_space = objective_zoo.sphere_function()

# Initialize custom wrapper
custom_wrapper = CustomWrapper(objective, search_space)
```
<br>

## Built-in Wrappers
OptiComp currently includes wrappers for the following libraries:

- **Optuna:** An optimization library for hyperparameter tuning.
- **bayes_opt:** A Bayesian Optimization library.
- **Hyperopt:** A library for distributed asynchronous hyperparameter optimization.
<br>

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to improve OptiComp.
<br>

## Documentation
For more detailed documentation and examples, please refer to the Wiki section of the GitHub repository.
