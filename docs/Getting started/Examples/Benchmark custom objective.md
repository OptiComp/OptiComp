# Benchmark Custom Objective

This example demonstrates how to use the `BenchmarkSuite` to compare and optimize using multiple wrappers from the `wrapper_zoo` with a custom objective.

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
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_random())
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_tpe())
benchmark_suite.add_wrapper(wrapper_zoo.fetch_bayesian())

# Compare and optimize using the added wrappers
results = benchmark_suite.benchmark(direction="maximize", max_steps=100, target_score=190, verbose=True, progress_bar=True)
```

This script sets up a benchmarking environment with a custom objective and search space, and then runs the optimization process to compare the performance of multiple wrappers.
