from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# Get common objective from objective_zoo
objective, search_space = objective_zoo.fetch_sphere_function()

# Create an instance of the benchmark_suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.optuna_random())
benchmark_suite.add_wrapper(wrapper_zoo.optuna_tpe())
benchmark_suite.add_wrapper(wrapper_zoo.bayesian())

# Compare and optimize using the added wrappers
results = benchmark_suite.benchmark(direction="minimize", max_steps=50, target_score=None, verbose=True, progress_bar=True)

results.summarize_all()
result = results.fetch_wrapper_result("optuna_random")
# result.wrapper.optimize
