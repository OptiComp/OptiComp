from dataclasses import dataclass

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from ..._core.wrapper_interface import WrapperInterface  # Replace with correct import path


class SklearnGridSearch(WrapperInterface):
    def __init__(self, param_grid, objective):
        super().__init__("3.6.1", "minimize", objective, param_grid)  # Adjust version and direction as needed
        self.param_grid = param_grid
        self.grid_search = None
        self.x_train = []
        self.y_train = []
    
    @dataclass
    class Config:
        num_samples: int = 30
        model = RandomForestClassifier()
    
    def _wrap_normalize_parameters(self, trial, search_space):
        # For sklearn's GridSearchCV, parameters are directly passed as a dictionary
        return trial.params

    def _wrap_setup(self, objective, search_space):
        # param_grid = {param_name: list(np.linspace(min_val, max_val, 10))
        #               for param_name, (min_val, max_val) in search_space.items()}
        param_grid = {
            'param1': np.linspace(-100, 100, 10),  # Example range for param1
            'param2': np.linspace(-100, 100, 10),  # Example range for param2
            'param3': np.linspace(-100, 100, 10)   # Example range for param3
        }

        print(param_grid)
        self.grid_search = GridSearchCV(self.Config.model, param_grid, scoring=objective, cv=5, verbose=1, n_jobs=-1)
        
        # Generate x_train
        self.x_train = []
        self.y_train = []
        for _ in range(self.Config.num_samples):
            params = {}
            for param_name, (min_val, max_val) in search_space.items():
                # Generate random values within the specified range for each parameter
                param_value = np.random.uniform(min_val, max_val)
                params[param_name] = param_value
            self.x_train.append(params)

        # Convert x_train to a list of dictionaries
        # Each dictionary represents a set of parameters to be tested
        self.x_train = [params for params in self.x_train]

        # Generate y_train (dummy values for illustration)
        self.y_train = np.random.rand(self.Config.num_samples)  # Replace with actual objective function evaluations if available

    def _wrap_step(self, objective, search_space):
        self.grid_search.fit(self.x_train, self.y_train)  # Replace with your own X_train, y_train data
        return self.grid_search.cv_results_['params'], self.grid_search.cv_results_['mean_test_score']   # Return current results after each step
