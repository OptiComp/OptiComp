import numpy as np

search_space = {'param1': (-100, 100),
                'param2': (-100, 100),
                'param3': (-100, 100)}


def objective(params: dict[str, float]) -> float:
    """
    Sphere function
    -----------
    The sphere function is a simple convex optimization problem where the goal is to minimize the sum of squares of all parameters.
    An optimizer is considered good at this function if it efficiently converges to the global minimum at [0, 0, ..., 0].

    ### Intended direction
    minimize
    """
    x = np.array(list(params.values()))
    return np.sum(x**2)
