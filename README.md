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
**Benchmark Common Wrappers And Objectives:**
```python
from opticomp import OptimizerSuite, objective_zoo, wrapper_zoo

# Get common objective from objective_zoo
objective, search_space = objective_zoo.sphere_function()

# Create an instance of the optimizer suite
optimizer_suite = OptimizerSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the optimizer_suite
optimizer_suite.add_wrapper(wrapper_zoo.optuna_random(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.optuna_tpe(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.bayesian(objective, search_space))

# Compare and optimize using the added wrappers
best_result, all_results = optimizer_suite.benchmark(direction="minimize", max_steps=100, target_score=200, verbose=True)
```

**Custom Wrappers:**
Create a custom wrapper by extending the WrapperInterface:

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

# Create an instance of the optimizer suite
optimizer_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the optimizer_suite
optimizer_suite.add_wrapper(wrapper_zoo.optuna_random(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.optuna_tpe(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.bayesian(objective, search_space))

# Compare and optimize using the added wrappers
best_result, all_results = optimizer_suite.benchmark(direction="maximize", max_steps=100, target_score=190, verbose=True)
```

**Selecting the Best Wrapper:**
```python
print("Haven't made this example yet")
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
