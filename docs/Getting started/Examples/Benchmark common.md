# Benchmark common

This example demonstrates how to use the `BenchmarkSuite` to compare and optimize using multiple wrappers from the `wrapper_zoo` and a common objective from the `objective_zoo`.

```python
from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# Get common objective from objective_zoo
objective, search_space = objective_zoo.fetch_sphere_function()

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_random())
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_tpe())
benchmark_suite.add_wrapper(wrapper_zoo.fetch_bayesian())

# Compare and optimize using the added wrappers
results = benchmark_suite.benchmark(direction="minimize", max_steps=100, target_score=200, verbose=True, progress_bar=True)
```

This script sets up a benchmarking environment with a common objective and multiple optimization wrappers, and then runs the optimization process to compare their performance.