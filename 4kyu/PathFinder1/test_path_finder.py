from unittest import TestCase
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

class TestPath_finder(TestCase):
    def test_path_finder(self):
        self.assertEqual(path_finder(a), True)
        self.assertEqual(path_finder(b), False)
        self.assertEqual(path_finder(c), True)
        self.assertEqual(path_finder(d), False)
