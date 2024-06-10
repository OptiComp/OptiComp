# Imports
from opticomp.optimizer_suite import OptimizerBenchmark
from opticomp.wrappers_control import Wrapper


# Example objective function
def objective(params):
    param1 = params['param1']
    param2 = params['param2']
    # param3 = params['param3']
    return (param1 - 2) ** 2 + (param2 + 3) ** 2

# Example search space
# {'param_name': (min, max)}
search_space = {'param1': (-100, 100),
                'param2': (-100, 100)}

# Select wrappers by name
wrapper_names = ["OptunaRandom", "OptunaTPE", "OptunaGridSearch", "BayesianOpt"]
selected_wrappers = [Wrapper.fetch(name) for name in wrapper_names]

# Create an instance of the optimizer benchmark
Optbenchmark = OptimizerBenchmark(objective, search_space)

# Add selected wrappers to the optimizer benchmark
for wrapper in selected_wrappers:
    Optbenchmark.add_wrapper(wrapper)

# Compare and optimize using the added wrappers
best_result, all_results = Optbenchmark.benchmark(direction="minimize", verbose=True)


