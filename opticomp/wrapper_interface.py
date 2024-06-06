# Wrapper interface
class WrapperInterface: 
    def __init__(self, objective, search_space):
        self.objective = objective
        self.search_space = search_space

    def optimize(self):
        raise NotImplementedError("This method should be overridden by subclasses")