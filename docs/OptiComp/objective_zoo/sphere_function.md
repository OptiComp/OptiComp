Module opticomp.objective_zoo.sphere_function
=============================================

Functions
---------

    
`objective(params: dict[str, float]) ‑> float`
:   Sphere function
    -----------
    The sphere function is a simple convex optimization problem where the goal is to minimize the sum of squares of all parameters.
    An optimizer is considered good at this function if it efficiently converges to the global minimum at [0, 0, ..., 0].