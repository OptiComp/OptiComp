# Wrapper interface
class WrapperInterface: 
    def __init__(self, objective, search_space):
        self.objective = objective
        self.search_space = search_space

    def norm_objective(self, params):
        return self.objective(params)

    def optimize(self):
        raise NotImplementedError("This method should be overridden by subclasses")