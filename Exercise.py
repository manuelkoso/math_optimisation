import abc


class Exercise(abc.ABC):
    @abc.abstractmethod
    def solve_exercise(self):
        """Solve exercise and display solution"""
        pass
