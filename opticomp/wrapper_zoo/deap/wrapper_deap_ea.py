import random
from dataclasses import dataclass

import numpy as np
from deap import algorithms, base, creator, tools

from opticomp import WrapperInterface


# Wrapper interface
class DeapEA(WrapperInterface):
    def __init__(self, objective, search_space):
        super().__init__("1.4.1", "maximize", objective, search_space)
        self.toolbox = base.Toolbox()
        self.population = None
        self.stats = None

    @dataclass
    class Config:
        # Delete this if the optimizer does not need any configuration variables
        population_size: type = 50
        generations: type = 30
        cxpb = 0.5
        mutpb = 0.2

    def _wrap_normalize_parameters(self, individual, search_space):
        normalized_params = {param_name: val for param_name, val in zip(search_space.keys(), individual)}
        return normalized_params
    
    def _wrap_setup(self, objective, search_space):
        
        # Define the individual and the population
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        # Register the individual attribute generators
        for param_name, (low, high) in search_space.items():
            self.toolbox.register(param_name, random.uniform, low, high)

        # # Register the structure initializers
        self.toolbox.register("individual", tools.initCycle, creator.Individual,
                      [getattr(self.toolbox, param_name) for param_name in search_space.keys()], n=1)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        def objective_wrapper(params):
            score = objective(params)
            return (score,)
        # Register the evaluation, crossover, mutation, and selection functions
        self.toolbox.register("evaluate", objective_wrapper)

        # Use CPU operators by default
        self.toolbox.register("mate", tools.cxBlend, alpha=0.5)
        self.toolbox.register("mutate", tools.mutPolynomialBounded,
                                low=[low for low, high in search_space.values()],
                                up=[high for low, high in search_space.values()],
                                eta=1.0, indpb=0.2)

        self.toolbox.register("select", tools.selTournament, tournsize=3)

        # Create an initial population
        self.population = self.toolbox.population(n=self.Config.population_size)

        # Statistics to keep track of the progress
        self.stats = tools.Statistics(lambda ind: ind.fitness.values)
        self.stats.register("avg", np.mean)
        self.stats.register("std", np.std)
        self.stats.register("min", np.min)
        self.stats.register("max", np.max)
            
    def _wrap_step(self, objective, search_space):
        # Run the genetic algorithm
        self.population, _ = algorithms.eaSimple(self.population, self.toolbox, self.Config.cxpb, self.Config.mutpb,
                                                    1, stats=self.stats, verbose=False)
        best_ind = tools.selBest(self.population, 1)[0]
        params = {param_name: val for param_name, val in zip(search_space.keys(), best_ind)}
        score = best_ind.fitness.values[0]
        return params, score
