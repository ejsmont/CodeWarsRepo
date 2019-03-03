"""
Task

You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1].
Number of climb rounds between adjacent locations is defined as difference of location altitudes
(ascending or descending).

Location altitude is defined as an integer number (0-9).

"""


def path_finder(area):
    return # total levels climbed


def maze_str_to_array(maze):
    """
    Function to convert string representation of a mountains into multidimensional list.
    :param maze: string representation of mountains
    :return: list representation of a mountains
    """
    return [[int(char) for char in row] for row in maze.split('\n')]


def hill_manhattan_distance(cell, goal):
    """
    Computes hill manhattan distance from some cell to the goal.
    Hill manhattan distance is defined as normal manhattan distance multiplied
    by 9 (maximal difference in elevation).
    :param cell: cell from where the distance is measured
    :param goal: goal node
    :return: integer value of a hill manhattan distance
    """
    return (abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])) * 9
