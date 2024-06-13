Module opticomp.objective_zoo.griewank_function
===============================================

Functions
---------

    
`objective(params: dict[str, float]) ‑> float`
:   Griewank function
    -----------
    The Griewank function is a multimodal optimization problem with many local minima and one global minimum.
    An optimizer is considered good at this function if it efficiently explores the search space to find the global minimum at [0, 0, ..., 0].