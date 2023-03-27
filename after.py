import itertools
from typing import Iterable, NamedTuple
import unittest

CostRow = tuple[int, ...]
CostMatrix = list[CostRow]
Assignment = tuple[int]

class CostedAssignment(NamedTuple):
    cost: int
    assignment: Assignment

def assignment(cost_matrix: CostMatrix) -> list[Assignment]:
    assignments = all_possible(cost_matrix)
    with_cost = costed(cost_matrix, assignments)
    return lowest_cost(with_cost)


def costed(cost_matrix: CostMatrix, assignments_to_price: Iterable[Assignment]) -> list[CostedAssignment]:
    return [
        CostedAssignment(cost_of_assignment(cost_matrix, assignment_to_price), assignment_to_price)
        for assignment_to_price in assignments_to_price
    ]


def lowest_cost(alternatives: list[CostedAssignment]) -> list[Assignment]:
    lowest_cost = min(alternatives).cost
    return [
        alternative.assignment for alternative in alternatives
        if alternative.cost == lowest_cost
    ]


def all_possible(cost_matrix: CostMatrix) -> Iterable[Assignment]:
    yield from itertools.permutations(
        range(len(cost_matrix))
    )


def cost_of_assignment(cost_matrix: CostMatrix, an_assignment: Assignment) -> int:
    return sum(
        cost_matrix[task][agent]
        for agent, task in enumerate(an_assignment)
    )


class TestAssignment(unittest.TestCase):
    def setUp(self) -> None:
        self.cost_matrix = [
            (14, 11, 6, 20, 12, 9, 4),
            (15, 28, 34, 4, 12, 24, 21),
            (16, 31, 22, 18, 31, 15, 23),
            (20, 18, 9, 15, 30, 4, 18),
            (24, 8, 24, 30, 28, 25, 4),
            (3, 23, 22, 11, 5, 30, 5),
            (13, 7, 5, 10, 7, 7, 32)
        ]

        self.optimal = [
            (2, 4, 6, 1, 5, 3, 0),
            (2, 6, 0, 1, 5, 3, 4)
        ]

    def test_should_return_optimal_assignment(self) -> None:
        self.assertEqual(assignment(self.cost_matrix), self.optimal)


if __name__ == '__main__':
    unittest.main()
