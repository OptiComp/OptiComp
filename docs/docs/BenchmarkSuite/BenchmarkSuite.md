# BenchmarkSuite

## Overview
The BenchmarkSuite is used to benchmark multiple optimization wrappers. You can easily benchmark and compare multiple wrappers on a common or custom objective. This way you can easily find the best optimizer for your purpose. 

<br>

## Methods

### `add_wrapper(self, wrapper)`

This method adds a wrapper to the the list of wrappers the BenchmarkSuite will use when benchmarking. This method also reinitializes any provided wrapper on the provided objective and search_space. It does this to make sure that all provided wrappers use the same objective and search_space.

#### Parameters
Provide a wrapper that you want to add to the benchmark list.

```python
wrapper: WrapperInterface
```

<br>

### `clear_wrappers(self)`

This method clears the wrapper list.


<br>

### `benchmark(self, direction, max_steps, target_score, verbose, progress_bar)`

This method is used to benchmark all the wrappers on the wrapper list. It will fully benchmark all wrappers and return the results in a `BenchmarkResult` class

#### Parameters
The following parameters can be used to configure the benchmark method.\
Set `direction` to 'minimize' or 'maximize'. This sets the direction for the optimizers.\
Either `max_steps` or `target_score` must be provided. You can also use both.\
Set `verbose` to `True` if you want to recieve extra information during the benchmark process.\
Set `progress_bar` to `True` if you want to see a progress bar for every wrapper.

```python
direction: str
max_steps: int = None
target_score: int = None
verbose: bool = True
progress_bar: bool = False
```


#### Returns
The `benchmark()` method returns all the results in a `BenchmarkResults` class. This class contains all the results and some useful methods to evaluate them.

```python
BenchmarkResults
```
