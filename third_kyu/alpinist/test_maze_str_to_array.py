from unittest import TestCase
from .alpinist import *

a = "\n".join([
  "000",
  "000",
  "000"
])

b = "\n".join([
  "010",
  "010",
  "010"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

d = "\n".join([
  "0707",
  "7070",
  "0707",
  "7070"
])

e = "\n".join([
  "700000",
  "077770",
  "077770",
  "077770",
  "077770",
  "000007"
])

f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

g = "\n".join([
  "000000",
  "000000",
  "000000",
  "000010",
  "000109",
  "001010"
])


class TestMazeStrToArray(TestCase):
    def test_maze_str_to_array(self):
        maze_arr = maze_str_to_array(b)
        expected = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.assertListEqual(expected, maze_arr)
        maze_arr = maze_str_to_array(d)
        expected = [[0, 7, 0, 7], [7, 0, 7, 0], [0, 7, 0 ,7], [7, 0, 7, 0]]
        self.assertListEqual(expected, maze_arr)

    def test_hill_manhattan_distance(self):
        cell = (0, 0)
        goal = (3, 3)
        self.assertEqual(54, hill_manhattan_distance(cell, goal))
        cell = (3, 3)
        self.assertEqual(0, hill_manhattan_distance(cell, goal))



