import itertools
import typing
import unittest

CostRow = tuple[int, ...]
CostMatrix = list[CostRow]
Assignment = tuple[int]

class Alternative(typing.NamedTuple):
    cost: int
    assignment: Assignment

def assignment(cost_matrix: CostMatrix) -> list[Assignment]:
    return cheapest_assignments(
        priced_assignments(
            cost_matrix,
            all_assignments(cost_matrix)
        )
    )


def all_assignments(cost_matrix: CostMatrix) -> typing.Iterable[Assignment]:
    yield from itertools.permutations(
        task_numbers(cost_matrix)
    )


def cheapest_assignments(alternatives: list[Alternative]) -> list[Assignment]:
    return [
        alternative.assignment for alternative in alternatives
        if alternative.cost == lowest_cost(alternatives)
    ]


def priced_assignments(cost_matrix, perms) -> list[Alternative]:
    return [
        Alternative(cost_of_permutation(cost_matrix, perm), perm) for perm in perms
    ]


def lowest_cost(alternatives) -> int:
    # This could be cached.
    return min(alternatives)[0]


def cost_of_permutation(cost_matrix: CostMatrix, permutation: tuple[int]) -> int:
    return sum(
        cost_matrix[task][agent]
        for agent, task in enumerate(permutation)
    )


def task_numbers(cost_matrix: CostMatrix):
    return range(len(cost_matrix))


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
