from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# Get common objective from objective_zoo
objective, search_space = objective_zoo.fetch_ackley_function()

search_space = {'param1': (-32.768, 32.768),
                'param2': (-32.768, 32.768)}

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_random())
benchmark_suite.add_wrapper(wrapper_zoo.fetch_optuna_tpe())
# benchmark_suite.add_wrapper(wrapper_zoo.fetch_deap_ea())

# Compare and optimize using the added wrappers
results = benchmark_suite.benchmark(direction="minimize", n_runs=20, max_steps=50, target_score=None, verbose=True, progress_bar=True)

results.plot_boxplot(show=True)

# results.plot_runs("deap_ea", show=True)

# result = results.fetch_wrapper_result("deap_ea")
# result.plot_objective_landscape(["param1", "param2"], resolution=100, show=True)
# result.plot_objective_landscape(["param1", "param2"], show_path=True, resolution=100, show=True)
# print(result.best_params)

# result = results.fetch_wrapper_result("optuna_tpe")
# result.plot_objective_landscape(["param1", "param2"], resolution=100, show=True)
# result.plot_objective_landscape(["param1", "param2"], show_path=True, resolution=100, show=True)
