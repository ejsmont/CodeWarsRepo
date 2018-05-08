"""
Task

You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.
"""


def path_finder(maze):
    maze_arr = maze_str_to_array(maze)
    n = len(maze_arr)
    start, goal = (0, 0), (n - 1, n - 1)
    from queue import Queue
    to_be_expanded = Queue()
    to_be_expanded.put(start)
    tree = set()

    while not to_be_expanded.empty():
        node = to_be_expanded.get()
        if node == goal:
            return True
        tree.add(node)
        get_node_neighbors(maze_arr, node, tree, to_be_expanded)
    return False


def maze_str_to_array(maze):
    """
    Function to convert string representation of a maze into multidimensional list. One (1) represents empty
    field, zero (0) represents a wall (impenetrable field)
    :param maze: string representation of a maze
    :return: list representation of a maze.
    """
    return [[1 if char == '.' else 0 for char in row] for row in maze.split('\n')]


def get_node_neighbors(maze_arr, parent_node, tree, to_be_expanded):
    """
    Computes a list of SearchNodes with all valid neighbors (except already seen nodes, walls and cells out of board)
    :param maze_arr: a multidim list containing the maze
    :param parent_node: a node for with neighbors are calculated
    :param tree: set of already expanded nodes
    :param to_be_expanded: a queue to which next nodes should be enqueued
    """
    n = len(maze_arr)
    x_0, y_0 = parent_node
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x_1 = x_0 + dx
        y_1 = y_0 + dy
        a = 0 <= x_1 < n and 0 <= y_1 < n and maze_arr[y_1][x_1] == 1
        b = (x_1, y_1) not in tree
        if a and b:
            to_be_expanded.put((x_1, y_1))
