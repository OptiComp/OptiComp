Module opticomp.objective_zoo.rosenbrock_function
=================================================

Functions
---------

    
`objective(params: dict[str, float]) ‑> float`
:   Rosenbrock function
    -----------
    The Rosenbrock function is a non-convex optimization problem with a narrow, parabolic valley.
    An optimizer is considered good at this function if it efficiently navigates the narrow valley to reach the global minimum at [1, 1, ..., 1].