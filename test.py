from opticomp import OptimizerSuite, objective_zoo, wrapper_zoo

objective, search_space = objective_zoo.rosenbrock_function()

# Create an instance of the optimizer suite
optimizer_suite = OptimizerSuite(objective, search_space)

optimizer_suite.add_wrapper(wrapper_zoo.optuna_random(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.optuna_tpe(objective, search_space))
optimizer_suite.add_wrapper(wrapper_zoo.bayesian(objective, search_space))

# Compare and optimize using the added wrappers
best_result, all_results = optimizer_suite.benchmark(direction="maximize", max_steps=50, target_score=None, verbose=True)
