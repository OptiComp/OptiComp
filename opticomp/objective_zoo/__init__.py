

def fetch_sphere_function():
    """
    Sphere function
    -----------
    The sphere function is a simple convex optimization problem where the goal is to minimize the sum of squares of all parameters.
    An optimizer is considered good at this function if it efficiently converges to the global minimum at [0, 0, ..., 0].
    
    Returns
    -------
    tuple
        A tuple containing the following elements:
        - Callable[[dict[str, float]], float]: The objective function.
        - dict[str, tuple[float, float]]: An example search space that fits the objective.
    """
    from .sphere_function import objective, search_space
    return objective, search_space


def fetch_griewank_function():
    """
    Griewank function
    -----------
    The Griewank function is a multimodal optimization problem with many local minima and one global minimum.
    An optimizer is considered good at this function if it efficiently explores the search space to find the global minimum at [0, 0, ..., 0].
    
    Returns
    -------
    tuple
        A tuple containing the following elements:
        - Callable[[dict[str, float]], float]: The objective function.
        - dict[str, tuple[float, float]]: An example search space that fits the objective.
    """
    from .griewank_function import objective, search_space
    return objective, search_space


def fetch_rosenbrock_function():
    """
    Rosenbrock function
    -----------
    The Rosenbrock function is a non-convex optimization problem with a narrow, parabolic valley.
    An optimizer is considered good at this function if it efficiently navigates the narrow valley to reach the global minimum at [1, 1, ..., 1].
    
    Returns
    -------
    tuple
        A tuple containing the following elements:
        - Callable[[dict[str, float]], float]: The objective function.
        - dict[str, tuple[float, float]]: An example search space that fits the objective.
    """
    from .rosenbrock_function import objective, search_space
    return objective, search_space


def fetch_ackley_function():
    """
    Ackley function
    -----------
    The Ackley function is a multimodal optimization problem with many local minima and one global minimum.
    An optimizer is considered good at this function if it efficiently escapes local minima and converges to the global minimum at [0, 0, ..., 0].
    
    Returns
    -------
    tuple
        A tuple containing the following elements:
        - Callable[[dict[str, float]], float]: The objective function.
        - dict[str, tuple[float, float]]: An example search space that fits the objective.
    """
    from .ackley_function import objective, search_space
    return objective, search_space
