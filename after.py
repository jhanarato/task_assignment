from itertools import permutations
import unittest

def assignment(cost: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    perms = task_agent_permutations(cost)
    alternatives = [
        (sum(cost[task][agent] for agent, task in enumerate(perm)), perm)
        for perm in perms
    ]
    m = min(alternatives)[0]
    return [ans for s, ans in alternatives if s == m]


def task_agent_permutations(cost: list[tuple[int, ...]]):
    return permutations(task_numbers(cost))


def task_numbers(cost):
    return range(number_of_tasks(cost))


def number_of_tasks(cost: list[tuple[int, ...]]) -> int:
    return len(cost)


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
