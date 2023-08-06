import random

from jmetal.core.problem import BinaryProblem, FloatProblem
from jmetal.core.solution import BinarySolution, FloatSolution

__author__ = "Antonio J. Nebro"


class OneMax(BinaryProblem):
    """ Class representing problem Kursawe """

    def __init__(self, number_of_bits: int = 256):
        self.number_of_bits = number_of_bits
        self.number_of_objectives = 1
        self.number_of_variables = 1
        self.number_of_constraints = 0

    def evaluate(self, solution: BinarySolution) -> None:
        counter_of_ones = 0
        for bits in solution.variables[0]:
            if bits:
                counter_of_ones += 1

        solution.objectives[0] = -1.0 * counter_of_ones

    def create_solution(self) -> BinarySolution:
        new_solution = BinarySolution(number_of_variables=1, number_of_objectives=1)
        new_solution.variables[0] = \
            [True if random.randint(0, 1) == 0 else False for i in range(self.number_of_bits)]
        return new_solution

    def get_name(self):
        return "OneMax"


class Sphere(FloatProblem):
    def __init__(self, number_of_variables: int = 10):
        super(Sphere, self).__init__()
        self.number_of_objectives = 1
        self.number_of_variables = number_of_variables
        self.number_of_constraints = 0

        self.lower_bound = [-5.12 for i in range(number_of_variables)]
        self.upper_bound = [5.12 for i in range(number_of_variables)]

        FloatSolution.lower_bound = self.lower_bound
        FloatSolution.upper_bound = self.upper_bound

    def evaluate(self, solution: FloatSolution):
        total = 0.0
        for x in solution.variables:
            total += x * x

        solution.objectives[0] = total

    def get_name(self):
        return "Sphere"
