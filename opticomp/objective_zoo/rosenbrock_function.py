import numpy as np

search_space = {'param1': (-10, 10),
                'param2': (-10, 10),
                'param3': (-10, 10)}


def objective(params: dict[str, float]) -> float:
    """
    Rosenbrock function
    -----------
    The Rosenbrock function is a non-convex optimization problem with a narrow, parabolic valley.
    An optimizer is considered good at this function if it efficiently navigates the narrow valley to reach the global minimum at [1, 1, ..., 1].

    ### Intended direction
    minimize
    """
    x = np.array(list(params.values()))
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)
