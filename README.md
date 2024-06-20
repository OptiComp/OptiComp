# OptiComp
[![PyPI Version](https://img.shields.io/pypi/v/OptiComp.svg)](https://pypi.org/project/OptiComp/)
[![License](https://img.shields.io/github/license/OptiComp/OptiComp.svg)](https://github.com/OptiComp/OptiComp/blob/main/LICENSE)

## Overview
OptiComp is a versatile library for comparing optimizers. It supports both built-in benchmark objectives and custom objectives. Users can compare various optimizers using provided wrappers or create their own. OptiComp streamlines finding the best optimizer for any task or an easy way to compare you optimizer against others.
<br>

## Features
- **Optimizer Comparison:** Compare different optimizer wrappers to find the most effective optimizer.
- **Visualization tools:** Utilize visualization tools to analyze the results from the optimizers.
- **Unified API:** Standardized optimizer API using common wrappers.
- **Standard Wrappers:** Ready-to-use wrappers.
- **Custom Wrappers:** Create your own wrappers any optimizer.
- **Standard Objectives:** Ready-to-use objective to evaluate an optimizer on.
- **Custom Objectives:** Create custom objectives to evaluate the optimizer on, allowing you to test optimizers on your project.
- **Direct Optimization:** Run optimizations directly using the provided wrappers.
<br>

## Installation
**Install OptiComp via pip:**

```
pip install opticomp
```
<br>

## Usage
#### **Benchmark Common Wrappers And Objectives:**
Use the OptiComp build-in wrappers and objectives:
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
For more specific examples, such as creating custom objectives or wrappers, please visit the [Wiki](https://github.com/OptiComp/OptiComp/wiki/Getting-started)

<br>

## Results
After running the library, you can expect the following information in the results:
- **Multiple Runs:** Keep multiple runs for every optimizer to test consistency.
- **Steps Taken:** Number of iterations or steps taken during the benchmarking.
- **Elapsed Time:** Total time taken for the algorithm to complete its task.
- **Best Score:** The score, or evaluation result after completing the benchmark.
- **Best Params:** Best parameters during benchmarking.
- **Score history:** A list with the score for every step taken. This can be visualised as shown below.
- **Params history:** A list with the output params for every step taken.
- **CPU and RAM history:** A list with the CPU and RAM usage during each step. This can be used to get the average or peaks.

#### Methods to visualise results

Score graph             |  Landscape graph
:-------------------------:|:-------------------------:
<img src="https://github.com/OptiComp/OptiComp/blob/main/docs/Img/example_summary.png" width="384" height="288">  |  <img src="https://github.com/OptiComp/OptiComp/blob/main/docs/Img/landscape_DeapEA.png" width="384" height="288">


These results provide insights into the performance and outcomes of each optimizer, enabling easy comparison between them.\
For more information, please visit the [results](https://github.com/OptiComp/OptiComp/wiki/Results) section in the wiki.

<br>

## Contributing

Contributions are welcome! Whether you're reporting a bug, suggesting a feature, or contributing code or wrappers, your help is appreciated. Please feel free to submit a pull request or open an issue to improve OptiComp. For more information, head to the [contributions](https://github.com/OptiComp/OptiComp/wiki/Contributing) section in the wiki.

<br>

## Documentation
For more detailed documentation and examples, please refer to the [Wiki](https://github.com/OptiComp/OptiComp/wiki) section of the GitHub repository.

