from abc import abstractmethod


class Solver:
    
    @abstractmethod
    def eval(self,function, var: int = 1) -> float:
        pass
    
    


