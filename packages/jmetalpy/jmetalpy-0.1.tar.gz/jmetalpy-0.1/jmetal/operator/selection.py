import random
from typing import List, TypeVar

from jmetal.component.density_estimator import CrowdingDistance
from jmetal.core.operator import Selection
from jmetal.util.comparator import dominance_comparator
from jmetal.util.ranking import DominanceRanking

""" Class implementing a best solution selection operator """

S = TypeVar('S')


class BinaryTournament(Selection[List[S], S]):
    def __init__(self):
        super(BinaryTournament, self).__init__()

    def get_name(self):
        return "Bynary tournament selection"

    def execute(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        elif len(solution_list) == 0:
            raise Exception("The solution is empty")

        if len(solution_list) == 1:
            result = solution_list[0]
        else:
            i, j = random.sample(range(0, len(solution_list)), 2)  # sampling without replacement
            solution1 = solution_list[i]
            solution2 = solution_list[j]

            flag = dominance_comparator(solution1, solution2)

            if flag == -1:
                result = solution1
            elif flag == 1:
                result = solution2
            else:
                result = [solution1, solution2][random.random() < 0.5]

        return result


class BestSolution(Selection[List[S], S]):
    def __init__(self):
        super(BestSolution, self).__init__()

    def execute(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        elif len(solution_list) == 0:
            raise Exception("The solution is empty")

        result = solution_list[0]
        for solution in solution_list[1:]:
            if dominance_comparator(solution, result) < 0:
                result = solution

        return result


class NaryRandomSolution(Selection[List[S], S]):
    def __init__(self, number_of_solutions_to_be_returned:int = 1):
        super(NaryRandomSolution, self).__init__()
        if number_of_solutions_to_be_returned < 0:
            raise Exception("The number of solutions to be returned must be positive integer")

        self.number_of_solutions_to_be_returned = number_of_solutions_to_be_returned

    def execute(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        if len(solution_list) == 0:
            raise Exception("The solution is empty")
        if len(solution_list)<self.number_of_solutions_to_be_returned:
            raise Exception("The solution list contains less elements then requred")

        # random sampling without replacement
        return random.sample(solution_list, self.number_of_solutions_to_be_returned)


class RandomSolution(Selection[List[S], S]):
    def __init__(self):
        super(RandomSolution, self).__init__()

    def execute(self, solution_list: List[S]) -> S:
        if solution_list is None:
            raise Exception("The solution list is null")
        elif len(solution_list) == 0:
            raise Exception("The solution is empty")

        return random.choice(solution_list)


class RankingAndCrowdingDistanceSelection(Selection[List[S], List[S]]):
    def __init__(self, max_population_size: int):
        super(RankingAndCrowdingDistanceSelection, self).__init__()
        self.max_population_size = max_population_size

    def execute(self, solution_list: List[S]) -> List[S]:
        ranking = DominanceRanking()
        crowding_distance = CrowdingDistance()
        ranking.compute_ranking(solution_list)

        ranking_index = 0
        new_solution_list = []

        while len(new_solution_list) < self.max_population_size:
            if len(ranking.get_subfront(ranking_index)) < self.max_population_size - len(new_solution_list):
                new_solution_list = new_solution_list + ranking.get_subfront(ranking_index)
                ranking_index += 1
            else:
                subfront = ranking.get_subfront(ranking_index)
                crowding_distance.compute_density_estimator(subfront)
                sorted_subfront = sorted(subfront, key=lambda x: x.attributes["distance"], reverse=True)
                for i in range((self.max_population_size - len(new_solution_list))):
                    new_solution_list.append(sorted_subfront[i])

        return new_solution_list
