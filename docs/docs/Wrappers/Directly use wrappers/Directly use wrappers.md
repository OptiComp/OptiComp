# Directly Use Wrappers

## Overview
You can also decide to directly use a wrapper to optimize. This way you can use any optimizer using a common API.

<br>

## Directly using a Wrapper
To directly use a wrapper, you need to follow these steps:

1. **Fetch or create a wrapper**: Fetch or create the wrapper you want to use.
2. **Initialization and Configuration**: Initialize the wrapper with the required parameters and configurations.
3. **Start Optimizing**: You can now directly start optimizing with the `optimize()` method provided by the `WrapperInterface`.

<br>

## Example

Below is an example of how you can directly use a wrapper for optimization. This example will utilize common objectives and wrappers, but everything works the same when you use custom objectives and wrappers.

```python
from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# For this example, we will use a common objective and search space
objective, search_space = objective_zoo.fetch_sphere_function()

# For this example, we will use a common wrapper
wrapper = wrapper_zoo.fetch_bayesian()

# Initialize the wrapper with the objective and search space
wrapper.initialize(objective, search_space)

# Start optimizing
result = wrapper.optimize('minimize', max_steps=100, target_score=200, progress_bar=True)
```
The `wrapper.optimize()` returns an instance of the `WrapperResult` class containing all the results from the optimization. 
