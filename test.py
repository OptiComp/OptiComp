from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# Get common objective from objective_zoo
objective, search_space = objective_zoo.fetch_ackley_function()

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_random())
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_tpe())
# benchmark_suite.add_wrapper(wrapper_zoo.fetch_bayesian())

# Compare and optimize using the added wrappers
results = benchmark_suite.benchmark(direction="maximize", max_steps=100, target_score=None, verbose=True, progress_bar=True)

results.summarize_all()

# results.plot(show=True, save_dir="docs")

result = results.fetch_wrapper_result("optuna_tpe")
# result.plot(show=True)

print(result.best_score)

# result.plot(show=True, save_dir="docs")
