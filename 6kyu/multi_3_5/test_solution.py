from unittest import TestCase
from .mult_3_5 import solution


class TestSolution(TestCase):
    def test_solution_for_10(self):
        self.assertEquals(solution(10), 23)

    def test_solution_for_12(self):
        self.assertEquals(solution(12), 33)

    def test_solution_for_1_and_0(self):
        self.assertEquals(solution(1), 0)
        self.assertEquals(solution(0), 0)
