import numpy as np


def sphere_function():
    """
    Sphere function.

    Explanation
    -----------
    The sphere function is a simple convex optimization problem where the goal is to minimize the sum of squares of all parameters.
    An optimizer is considered good at this function if it efficiently converges to the global minimum at [0, 0, ..., 0].
    """
    search_space = {'param1': (-100, 100),
                    'param2': (-100, 100),
                    'param3': (-100, 100)}
    
    def objective(params):
        x = np.array(list(params.values()))
        return np.sum(x**2)
    
    return objective, search_space


def griewank_function():
    """
    Griewank function.

    Explanation
    -----------
    The Griewank function is a multimodal optimization problem with many local minima and one global minimum. 
    An optimizer is considered good at this function if it efficiently explores the search space to find the global minimum at [0, 0, ..., 0].
    """
    search_space = {'param1': (-600, 600),
                    'param2': (-600, 600),
                    'param3': (-600, 600)}
    
    def objective(params):
        x = np.array(list(params.values()))
        n = len(x)
        return 1 + (1 / 4000) * np.sum(x**2) - np.prod(np.cos(x / np.sqrt(np.arange(1, n + 1))))
    
    return objective, search_space


def rosenbrock_function():
    """
    Rosenbrock function.

    Explanation
    -----------
    The Rosenbrock function is a non-convex optimization problem with a narrow, parabolic valley.
    An optimizer is considered good at this function if it efficiently navigates the narrow valley to reach the global minimum at [1, 1, ..., 1].
    """
    search_space = {'param1': (-10, 10),
                    'param2': (-10, 10),
                    'param3': (-10, 10)}
    
    def objective(params):
        x = np.array(list(params.values()))
        return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)
    
    return objective, search_space


def ackley_function():
    """
    Ackley function.

    Explanation
    -----------
    The Ackley function is a multimodal optimization problem with many local minima and one global minimum.
    An optimizer is considered good at this function if it efficiently escapes local minima and converges to the global minimum at [0, 0, ..., 0].
    """

    search_space = {'param1': (-32.768, 32.768),
                    'param2': (-32.768, 32.768),
                    'param3': (-32.768, 32.768)}
    
    def objective(params):
        x = np.array(list(params.values()))
        n = len(x)
        return -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / n)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / n)
    
    return objective, search_space