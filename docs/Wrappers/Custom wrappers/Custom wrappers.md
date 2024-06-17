# Custom Wrappers

## Overview
Custom wrappers are user-defined extensions to the core classes, allowing you to easily create a wrapper for any library. This enables a standardized approach to handling various optimization libraries.

<br>

## Creating a Custom Wrapper
To create a custom wrapper, you need to follow these steps:

1. **Define the Wrapper Class**: Create a new class that inherits from `WrapperInterface`.
2. **Implement Required Methods**: Override the necessary methods to customize the behavior of the wrapper.
3. **Initialization and Configuration**: Initialize the wrapper with the required parameters and configurations.

<br>

## Template

Below is a template for creating a custom wrapper. This template outlines the necessary structure and methods you need to implement.

```python
from dataclasses import dataclass
from opticomp import WrapperInterface
import some_optimizer_library

# Wrapper interface
class CustomWrapper(WrapperInterface):
    def __init__(self, objective, search_space):
        super().__init__("version", "default_direction", objective, search_space)

    @dataclass
    class Config:
        # Delete this if the optimizer does not need any configuration variables
        setting: type = default_value
        hyperparameter: type = default_value

    def _wrap_normalize_parameters(self, params, search_space):
        # Normalize parameters if needed
        return normalized_params
    
    def _wrap_setup(self, objective, search_space):
        # Setup the optimizer
        # This code only gets called once, at the start of the optimization loop
            
    def _wrap_step(self, objective, search_space):
        # Take ONE step with the optimizer.
        return best_params, best_score
```
<br>


## Explanation
Here is a detailed explanation of each part of the custom wrapper setup.

### `__init__(self, objective, search_space)`
The initialization method sets up the wrapper with the necessary parameters. It calls the parent WrapperInterface's init method with the version, default direction (either 'minimize' or 'maximize'), the objective function, and the search space.

```python
def __init__(self, objective, search_space):
    super().__init__("version", "default_direction", objective, search_space)
```
<br>

### `Config`
The Config class, decorated with @dataclass, holds configuration parameters for the optimizer. You can delete this class if the optimizer does not need any configuration variables.

```python
@dataclass
class Config:
    setting: type = default_value
    hyperparameter: type = default_value
```
<br>

### `_wrap_normalize_parameters(self, params, search_space)`
This method normalizes parameters if necessary. It takes parameters output from the library as input, normalizes them, and returns the normalized parameters. These normalized parameters are then used in the user-provided `objective` function to compute a score.

```python
def _wrap_normalize_parameters(self, params, search_space):
    # Normalize parameters if needed
    return normalized_params

```
- Attributes\
The params are the output parameters of the library. This is library specific.
The search space is provided by the user when initializing the wrapper.
```python
params: # Library specific
search_space: dict[str, tuple[float, float]]
```

- Return\
You can use the provided search_space for the normilized_params strings.
```python
normilized_params: dict[str, float]
```
<br>

### `_wrap_setup(self, objective, search_space)`
The _wrap_setup method is responsible for setting up the optimizer. This code is only called once at the start of the optimization loop.

```python
def _wrap_setup(self, objective, search_space):
    # Setup the optimizer
    # This code only gets called once, at the start of the optimization loop
```

- Attributes\
The objective function and search space are provided by the user when initializing the wrapper.

```python
objective: Callable[[dict[str, float]], float]
search_space: dict[str, tuple[float, float]]
```
<br>

### `_wrap_step(self, objective, search_space)`
The _wrap_step method performs a single optimization step. It is important that it takes only one step with the optimizer. This will allow us to catch extra information and implement early stopping. It returns the best parameters and the best score found so far.

```python
def _wrap_step(self, objective, search_space):
    # Take ONE step with the optimizer
    return best_params, best_score
```

- Attributes\
The objective function and search space are provided by the user when initializing the wrapper.

```python
objective: Callable[[dict[str, float]], float]
search_space: dict[str, tuple[float, float]]
```


-  Return\
Return the best_params and best_score. You can use the provided search_space for the best_params strings.

```python
best_params: dict[str, float]
best_score: float
```
