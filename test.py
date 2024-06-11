from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# Get common objective from objective_zoo
objective, search_space = objective_zoo.sphere_function()

# Create an instance of the optimizer suite
optimizer_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the optimizer_suite
optimizer_suite.add_wrapper(wrapper_zoo.optuna_random(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.optuna_tpe(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.bayesian(objective, search_space))

# Compare and optimize using the added wrappers
best_result, all_results = optimizer_suite.benchmark(direction="minimize", max_steps=100, target_score=200, verbose=True)
