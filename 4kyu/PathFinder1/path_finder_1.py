"""
Task

You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.
"""


class SearchNode(object):
    """
    A class representing a node. It stores information about a parent node, children nodes, coordinates.
    Can compare two nodes using theirs coordinates.
    """

    def __init__(self, parent_node, x, y):
        self.parent_node = parent_node
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y


def path_finder(maze):
    maze_arr = maze_str_to_array(maze)
    n = len(maze_arr)
    start, goal = (0, 0), (n - 1, n - 1)
    init_node = SearchNode(None, start[0], start[1])
    return None


def maze_str_to_array(maze):
    """
    Function to convert string representation of a maze into multidimensional list. One (1) represents empty
    field, zero (0) represents a wall (impenetrable field)
    :param maze: string representation of a maze
    :return: list representation of a maze.
    """
    return [[1 if char == '.' else 0 for char in row] for row in maze.split('\n')]





