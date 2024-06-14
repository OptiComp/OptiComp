# WrapperInterface

## Overview
The WrapperInterface is the heart of every wrapper in OptiComp. It simplifies the creation of wrappers and provides an easy way to use them. The WrapperInterface provides a few public methods.

<br>

## Methods

### `initialize(self, objective, search_space)`

This method initializes or reinitializes a wrapper, allowing you to change the objective and search_space the wrapper will use during optimization. The `BenchmarkSuite` automatically reinitializes wrappers to ensure every provided wrapper uses the same objective and search_space.

#### Parameters
The provided objective and search_space can be manually created or taken from the `objective_zoo`.

```python
objective: Callable[[dict[str, float]], float]
search_space: dict[str, tuple[float, float]]
```

<br>

### `optimize(self, direction, max_steps, target_score, progress_bar)`

The optimize method is used to optimize the parameters using the provided `search_space` and `objective`. This method is also used by the `BenchmarkSuite` when comparing multiple wrappers.

#### Parameters
The following parameters can be used to configure the optimize method. Either `max_steps` or `target_score` must be provided. You can also use both.

```python
direction: str
max_steps: int = None
target_score: float = None
progress_bar: bool = False
```


#### Returns
The `optimize()` method returns all the results in a `WrapperResult` class. This class contains all the results and some useful methods to evaluate them.

```python
WrapperResult
```
