from unittest import TestCase
from .longst_substr import longest


class TestLongest(TestCase):
    def test_longest(self):
        input_str = 'a'
        self.assertEquals(longest(input_str), 'a')
