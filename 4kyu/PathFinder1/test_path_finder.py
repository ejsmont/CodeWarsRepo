from unittest import TestCase
from .path_finder_1 import path_finder
from .path_finder_1 import SearchNode

a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])


class TestPathFinder(TestCase):

    # def test_path_finder(self):
    #     self.assertEqual(path_finder(a), True)
    #     self.assertEqual(path_finder(b), False)
    #     self.assertEqual(path_finder(c), True)
    #     self.assertEqual(path_finder(d), False)

    def test_node_class(self):
        first = SearchNode(None, 0, 0)
        second = SearchNode(first, 1, 1)
        first_another = SearchNode(None, 0, 0)
        self.assertEqual(True, first is second.parent_node)
        self.assertEqual(False, second is first.parent_node)
        self.assertEqual(0, first.x)
        self.assertEqual(0, first.y)
        self.assertEqual(1, second.x)
        self.assertEqual(1, second.y)
        self.assertEqual(False, first == second)
        self.assertEqual(True, first == first_another)