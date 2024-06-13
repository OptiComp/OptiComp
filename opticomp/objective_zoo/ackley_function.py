import numpy as np

search_space = {'param1': (-32.768, 32.768),
                'param2': (-32.768, 32.768),
                'param3': (-32.768, 32.768)}


def objective(params: dict[str, float]) -> float:
    """
    Ackley function
    -----------
    The Ackley function is a multimodal optimization problem with many local minima and one global minimum.
    An optimizer is considered good at this function if it efficiently escapes local minima and converges to the global minimum at [0, 0, ..., 0].
    """
    x = np.array(list(params.values()))
    n = len(x)
    return -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / n)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / n)
