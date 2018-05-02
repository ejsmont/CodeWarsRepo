"""
Task

You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.
"""


def path_finder(maze):
    maze_arr = maze_str_to_array(maze)
    n = len(maze_arr)

    return None


def maze_str_to_array(maze):
    """
    Function to convert string representation of a maze into multidimensional list. One (1) represents empty
    field, zero (0) represents a wall (impenetrable field)
    :param maze: string representation of a maze
    :return: list representation of a maze.
    """
    return [[1 if char == '.' else 0 for char in row] for row in maze.split('\n')]

