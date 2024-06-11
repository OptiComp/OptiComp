from opticomp import BenchmarkSuite, wrapper_zoo


# Custom objective
def objective(params):
    # Split params
    param1 = params['param1']
    param2 = params['param1']
    
    # Evaluate and calculate score
    score = param1 + param2

    # Return score
    return score

# Custom search_space
search_space = {'param1': (-100, 100),
                'param2': (-100, 100)}

# Create an instance of the benchmark suite
benchmark_suite = BenchmarkSuite(objective, search_space)

# Add wrappers directly from wrapper_zoo to the benchmark_suite
benchmark_suite.add_wrapper(wrapper_zoo.optuna_random(objective, search_space))
benchmark_suite.add_wrapper(wrapper_zoo.optuna_tpe(objective, search_space))
benchmark_suite.add_wrapper(wrapper_zoo.bayesian(objective, search_space))

# Compare and optimize using the added wrappers
best_result, all_results = benchmark_suite.benchmark(direction="maximize", max_steps=100, target_score=190, verbose=True)
