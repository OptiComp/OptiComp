# OptiComp
## Overview
OptiComp is a versatile optimization library designed to streamline the comparison of optimizers. With a straightforward approach, it facilitates the assessment of various optimizers by providing standard benchmark objectives. Whether utilizing built-in benchmarks or custom objectives, OptiComp empowers users to identify the most suitable optimizer for their specific goals. The library offers convenient wrappers for comparing optimizer libraries or enables users to create their own wrappers as needed. Simplifying the process, OptiComp empowers users to easily compare optimizers and determine the best fit for their optimization tasks.

## Features
- **Unified API:** Standardize different optimization libraries or custom optimizers with common wrappers.
- **Standard Wrappers:** Ready-to-use wrappers for popular optimization libraries like Optuna, bayes_opt, and Hyperopt.
- **Custom Wrappers:** Create your own wrappers for other libraries or your custom optimizers.
- **Standard Objectives:** Pick a standard objective to evaluate the optimizer on, providing predefined metrics for easier evaluation and comparison across different optimization algorithms.
- **Custom Objectives:** Create custom objectives to evaluate the optimizer on, allowing for tailored evaluation metrics based on specific tasks or requirements.
- **Optimizer Comparison:** Compare different wrappers on your objective to find the most effective optimizer.
- **Best Optimizer Selection:** Select the best wrapper for your objective with less computational overhead.
- **Direct Optimization:** Run optimizations directly using the provided wrappers.

## Installation
**Install OptiComp via pip:**

```
pip install opticomp
```

## Usage
**Benchmark Built-in Wrappers:**
```python
# Imports
from opticomp.benchmarking import OptimizerBenchmark
from opticomp.wrappers_control import Wrapper

# Example objective function
def objective(params):
    param1 = params['param1'] 
    param2 = params['param2'] 
    # param3 = params['param3'] 
    return (param1 - 2) ** 2 + (param2 + 3) ** 2

# Example search space
# {'param_name': (min, max)}
search_space = {'param1': (-100, 100), 
                'param2': (-100, 100)}

# Select wrappers by name
wrapper_names = ["OptunaRandom", "OptunaTPE", "OptunaGridSearch", "BayesianOpt"]
selected_wrappers = [Wrapper.fetch(name) for name in wrapper_names]

# Create an instance of the optimizer benchmark
Optbenchmark = OptimizerBenchmark(objective, search_space)

# Add selected wrappers to the optimizer benchmark
for wrapper in selected_wrappers:
    Optbenchmark.add_wrapper(wrapper)

# Compare and optimize using the added wrappers
best_result, all_results = Optbenchmark.benchmark(verbose=True)
```

**Comparing Wrappers:**

```python
print("Haven't made this shit yet")
```

**Custom Wrappers:**
Create a custom wrapper by extending the WrapperInterface:

```python
print("Haven't made this shit yet")
```

**Selecting the Best Wrapper:**
```python
print("Haven't made this shit yet")
```

## Built-in Wrappers
OptiComp currently includes wrappers for the following libraries:

- **Optuna:** An optimization library for hyperparameter tuning.
- **bayes_opt:** A Bayesian Optimization library.
- **Hyperopt:** A library for distributed asynchronous hyperparameter optimization.


## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to improve OptiComp.

## Documentation
For more detailed documentation and examples, please refer to the Wiki section of the GitHub repository.
