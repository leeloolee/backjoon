import unittest
from solutions.InsertOperator import solution

class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(2, [5, 6], [0, 0, 1, 0]), (30, 30))

    def test_solution3(self):
        self.assertEqual(solution(3, [3, 4, 5], [1, 0, 1, 0]), (35, 17))
