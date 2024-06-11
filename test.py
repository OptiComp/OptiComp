import numpy as np

from opticomp import OptimizerSuite, wrapper_zoo

'''
Performance on the Sphere function signifies an optimizer's effectiveness in finding the global minimum,
situated at the origin with a function value of 0.
It reflects the optimizer's ability to efficiently explore the search space,
navigate towards the optimal solution,
and converge to the global minimum with minimal iterations or evaluations.
'''


# sphere function
def objective(params):
    x = np.array([params[key] for key in params.keys()])
    return np.sum(x**2)

# Search space
# {'param_name': (min, max)}
search_space = {'param1': (-100, 100),
                'param2': (-100, 100),
                'param3': (-100, 100)}

# Create an instance of the optimizer suite
optimizer_suite = OptimizerSuite(objective, search_space)

optimizer_suite.add_wrapper(wrapper_zoo.optuna_random(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.optuna_tpe(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.bayesian(objective, search_space))

# Compare and optimize using the added wrappers
best_result, all_results = optimizer_suite.benchmark(direction="maximize", max_steps=500, target_score=29000, verbose=True)

opt = wrapper_zoo.optuna_random(objective, search_space)
opt.optimize
