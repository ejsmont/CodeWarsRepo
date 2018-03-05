from unittest import TestCase
from .mult_3_5 import solution

class TestSolution(TestCase):
    def test_solution(self):
        self.assertEquals(solution(10), 23)
