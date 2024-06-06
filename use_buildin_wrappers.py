# Imports
from opticomp.optimizer_compare import OptimizerCompare
from opticomp.wrappers_buildin import select_wrapper

# Objective function
def objective(params):
    x, y = params
    return (x - 2) ** 2 + (y + 3) ** 2

# Search space
search_space = {'x': (-10, 10), 
                'y': (-10, 10)}

# Select wrappers by name
wrapper_names = ["OptunaRandom", "OptunaTPE"]
selected_wrappers = [select_wrapper(name) for name in wrapper_names]

# Create an instance of the optimizer comparer
OptComparer = OptimizerCompare(objective, search_space)

# Add selected wrappers to the optimizer comparer
for wrapper in selected_wrappers:
    OptComparer.add_wrapper(wrapper)

# Compare and optimize using the added wrappers
best_result, all_results = OptComparer.compare(verbose=True)

# print(f"Best optimizer: {best_result}")
# print("All results:", all_results)

