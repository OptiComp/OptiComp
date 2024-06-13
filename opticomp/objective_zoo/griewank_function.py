import numpy as np

search_space = {'param1': (-600, 600),
                'param2': (-600, 600),
                'param3': (-600, 600)}


def objective(params: dict[str, float]) -> float:
    """
    Griewank function
    -----------
    The Griewank function is a multimodal optimization problem with many local minima and one global minimum.
    An optimizer is considered good at this function if it efficiently explores the search space to find the global minimum at [0, 0, ..., 0].
    """
    x = np.array(list(params.values()))
    n = len(x)
    return 1 + (1 / 4000) * np.sum(x**2) - np.prod(np.cos(x / np.sqrt(np.arange(1, n + 1))))
