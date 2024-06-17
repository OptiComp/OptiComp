# Fetching a Common Wrapper

## Overview
OptiComp provides a set of common wrappers. This allows you to quickly set up and start optimizing without having to manually configure a wrapper.

## Steps to Fetch a Common Wrapper
To fetch a common wrapper, you need to follow these steps:

1. **Import the Wrapper Zoo**: Import the `wrapper_zoo` module from the library.
2. **Fetch the Wrapper**: Use the appropriate method from `wrapper_zoo` to fetch the desired wrapper.
3. **Use the Wrapper**: The fetched wrapper can now be given to the `BenchmarkSuite` or directly used to optimize

## Example
Below is an example of how you can fetch a common wrapper. We will use a common objective and search_space for an example

```python
from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# Fetch a common objective and search space
objective, search_space = objective_zoo.fetch_sphere_function()

# Fetch a common wrapper
wrapper = wrapper_zoo.fetch_bayesian()

# Fetch and initialize a common wrapper
initialized_wrapper = wrapper_zoo.fetch_bayesian(objective, search_space)

# The wrapper will be automatically initialized or reinitialized when adding it to the BenchmarkSuite
```
