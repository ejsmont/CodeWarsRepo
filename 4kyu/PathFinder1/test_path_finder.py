from unittest import TestCase
from queue import Queue

from .path_finder_1 import maze_str_to_array
from .path_finder_1 import get_node_neighbors
from .path_finder_1 import path_finder


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

    def test_maze_str_to_array(self):
        maze_arr = maze_str_to_array(a)
        expected = [[1, 0, 1], [1, 0, 1], [1, 1, 1]]
        self.assertListEqual(expected, maze_arr)
        maze_arr = maze_str_to_array(b)
        expected = [[1, 0, 1], [1, 0, 1], [0, 1, 1]]
        self.assertListEqual(expected, maze_arr)

    def test_get_neighbors(self):
        maze_arr = maze_str_to_array(a)
        parent = (0, 2)
        to_be_expanded = Queue()
        tree = {parent}
        get_node_neighbors(maze_arr, parent, tree, to_be_expanded)
        expected = [(0, 1), (1, 2)]
        while not to_be_expanded.empty():
            child = to_be_expanded.get()
            tree.add(child)
            self.assertEqual(True, child in expected)
        next_parent = (1, 2)
        expected = [(2, 2)]
        get_node_neighbors(maze_arr, next_parent, tree, to_be_expanded)
        while not to_be_expanded.empty():
            child = to_be_expanded.get()
            self.assertNotEqual(parent, child)
            self.assertEqual(True, child in expected)

    def test_path_finder(self):
        self.assertEqual(path_finder(a), True)
        self.assertEqual(path_finder(b), False)
        self.assertEqual(path_finder(c), True)
        self.assertEqual(path_finder(d), False)