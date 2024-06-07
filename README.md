# OptiComp
## Overview
OptiComp is a versatile optimization library that provides a unified interface for various optimization libraries, including Optuna, bayes_opt, and Hyperopt. With OptiComp, you can efficiently optimize your objectives using built-in wrappers or create custom ones tailored to your needs. One of the standout features of OptiComp is its ability to compare different optimizers and select the best one for your specific requirements, making it an invaluable tool for anyone looking to streamline and enhance their optimization workflows.

## Features
- **Unified API:** Standardize different optimization libraries or custom optimizers with common wrappers.
- **Built-in Wrappers:** Ready-to-use wrappers for popular optimization libraries like Optuna, bayes_opt, and Hyperopt.
- **Custom Wrappers:** Create your own wrappers for other libraries or your custom optimizers.
- **Direct Optimization:** Run optimizations directly using the provided wrappers.
- **Optimizer Comparison:** Compare different wrappers on your objective to find the most effective optimizer.
- **Best Wrapper Selection:** Select the best wrapper for your objective with less computational overhead.

## Installation
**Install OptiComp via pip:**

```
pip install opticomp
```

## Usage
**Using Built-in Wrappers:**
```python
from opticomp import select_wrapper

# Example objective function
def objective(params):
    x = params['x']
    y = params['y']
    return -(x ** 2 + y ** 2)

# Select a wrapper
OptunaWrapper = select_wrapper('OptunaRandom')

# Initialize the wrapper
optimizer = OptunaWrapper(search_space={'x': (-10, 10), 'y': (-10, 10)})

# Run optimization
best_params, best_score = optimizer.optimize(objective)

print(f"Best Parameters: {best_params}, Best Score: {best_score}")
```

**Comparing Wrappers:**

```
from opticomp import compare_wrappers

# List of wrapper names to compare
wrapper_names = ['OptunaRandom', 'OptunaTPE', 'HyperoptTPE', 'BayesianOpt']

# Compare the wrappers on the objective
results = compare_wrappers(objective, wrapper_names, search_space={'x': (-10, 10), 'y': (-10, 10)})

for result in results:
    print(f"Wrapper: {result['wrapper']}, Best Params: {result['params']}, Best Score: {result['score']}")
```

**Custom Wrappers:**
Create a custom wrapper by extending the WrapperInterface:

```
from opticomp.wrapper_interface import WrapperInterface

class CustomOptimizerWrapper(WrapperInterface):
    name = "CustomOptimizer"
    library_version = "1.0.0"
    default_direction = "maximize"

    def optimize(self, objective):
        # Implement your custom optimization logic here
        pass
```

**Selecting the Best Wrapper:**
```
from opticomp import select_best_wrapper

# Select the best wrapper for the objective
best_wrapper_name = select_best_wrapper(objective, ['OptunaRandom', 'OptunaTPE', 'HyperoptTPE', 'BayesianOpt'])
print(f"The best wrapper is: {best_wrapper_name}")
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
