import inspect

from opticomp import BenchmarkSuite, objective_zoo, wrapper_zoo

# Get common objective from objective_zoo
objective, search_space = objective_zoo.fetch_sphere_function()

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)


# Get and filter all wrappers
members = inspect.getmembers(wrapper_zoo, inspect.isfunction)
fetch_functions = [func for name, func in members if name.startswith('fetch_')]
# Add each wrapper to the benchmark suite
for fetch_func  in fetch_functions:
    print(f"Fetching {fetch_func.__name__}:")
    benchmark_suite.add_wrapper(fetch_func())


# Maximize all wrappers
results = benchmark_suite.benchmark(direction="maximize", max_steps=10)

# Minimize all wrappers
results = benchmark_suite.benchmark(direction="minimize", max_steps=10)

# Summarize all
results.summarize_all()
