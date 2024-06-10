# Imports
import numpy as np

from opticomp.benchmarking import OptimizerBenchmark
from opticomp.wrappers_control import Wrapper

# Objective function
# def objective(params):
#     param1 = params['param1']
#     param2 = params['param2']
#     # param3 = params['param3']
#     return (param1 - 2) ** 2 + (param2 + 3) ** 2 # - (param3 + 3) ** 2

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
                'param3': (-100, 100),
                'param4': (-100, 100),
                'param5': (-100, 100),
                'param6': (-100, 100)}

# Select wrappers by name
wrapper_names = ["OptunaRandom", "OptunaTPE", "OptunaGridSearch", "BayesianOpt", "HyperoptTPE"]
selected_wrappers = [Wrapper.fetch(name) for name in wrapper_names]

for wrapper in selected_wrappers:
    Wrapper.print_info(wrapper)

# Create an instance of the optimizer comparer
Optbenchmark = OptimizerBenchmark(objective, search_space)

# Add selected wrappers to the optimizer comparer
for wrapper in selected_wrappers:
    Optbenchmark.add_wrapper(wrapper)

# Compare and optimize using the added wrappers
best_result, all_results = Optbenchmark.benchmark(direction="maximize", verbose=True)

# print(f"Best optimizer: {best_result}")
# print("All results:", all_results)

