# Wrapper interface
class WrapperInterface: 
    def __init__(self, objective, search_space):
        self.objective = objective
        self.search_space = search_space

    def norm_objective(self, params):
        raise NotImplementedError("This method should be overridden to normalize the parameters for the optimizer")

    def optimize(self):
        raise NotImplementedError("This method should be overridden by subclasses")