import time
import heapq

class PathFinding:
    def __init__(self, maze):
        self.maze = maze
        self.start_pos = []  # represented by an ordered list such as [x, y]
        self.goal_pos = []
        self.initialize_start_goal_states()

    def initialize_start_goal_states(self):
        """
        Finds the location of start and goal states of the maze, represented by ordered lists
        consisting of row and column positions, that is, [a, b] represents a state at row a and column b.
        """
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 'S':
                    self.start_pos = [i, j]
                elif self.is_goal(i, j):
                    self.goal_pos = [i, j]

    def get_neighbors_up_down(current):
        """
        Find neighbors for the current point
        :return: a list of neighbors for current point
        """
        all_neighbor=[]
        all_neighbor.append((current[0] - 1, current[1]))
        all_neighbor.append((current[0] + 1, current[1]))
        all_neighbor.append((current[0], current[1] - 1))
        all_neighbor.append((current[0], current[1] + 1))

        neighbot=[]
        for i in all_neighbor:
            if isopen
                """
                Working on
                """

    def greedy_search_up_down(self):
        """
        Find the path from start to goal using greedy search in a maze where you can only move up, down, left, or right.
        For example: [[Start_x, Start_y],[a, b], [Goal_x, Goal_y]] means that the agent takes the path
                    Start -> [a, b] -> Goal.
        :return: a list of ordered lists containing states of the path.
        """
        heap = []
        heapq.heappush(heap, (self.start_pos, 0))
        game_from = {}
        game_from[0]= null

        while len(heap)!=0:
            current = heapq.heappop()

            if current[1] == self.goal_pos: # break if goal found
                break
        """
        Still Working On
        """

        return []

    def a_star_search_up_down(self):
        """
        Find the path from start to goal using A* search in a maze where you can only move up, down, left, or right.
        For example: [[Start_x, Start_y],[a, b], [Goal_x, Goal_y]] means that the agent takes the path
                    Start -> [a, b] -> Goal.
        :return: a list of ordered lists containing states of the path.
        """
        return []

    def greedy_search_diagonal(self):
        """
        Find the path from start to goal using greedy search in a maze where you can also move diagonally.
        For example: [[Start_x, Start_y],[a, b], [Goal_x, Goal_y]] means that the agent takes the path
                    Start -> [a, b] -> Goal.
        :return: a list of ordered lists containing states of the path.
        """
        return []

    def a_star_search_diagonal(self):
        """
        Find the path from start to goal using A* search in a maze where you can also move diagonally.
        For example: [[Start_x, Start_y],[a, b], [Goal_x, Goal_y]] means that the agent takes the path
                    Start -> [a, b] -> Goal.
        :return: a list of ordered lists containing states of the path.
        """
        return []

    def manhattan_heuristic(self, x, y):
        """
        Calculates the Manhattan heuristic at the state [x, y].
        This is the Manhattan distance between the given state and the goal state.
        :param x: row index
        :param y: column index
        :return: a value representing the Manhattan heuristic of at given state.
        """
        return self.manhattan_distance(x, y, self.goal_pos[0], self.goal_pos[1])

    def manhattan_distance(self, x1, y1, x2, y2):
        """
        Calculates the Manhattan distance between [x1, y1] and [x2, y2]
        :param x1: row index of first state
        :param y1: column index of first state
        :param x2: row index of second state
        :param y2: column index of second state
        :return: the Manhattan distance between the states.
        """
        return abs(x1 - x2) + abs(y1 - y2)

    def chebyshev_heuristic(self, x, y):
        """
        Calculates the Chebyshev heuristic at the state [x, y].
        This is the Chebyshev distance between the given state and the goal state.
        :param x: x index
        :param y: column index
        :return: a value representing the Chebyshev heuristic of at given state.
        """
        return self.chebyshev_distance(x, y, self.goal_pos[0], self.goal_pos[1])

    def chebyshev_distance(self, x1, y1, x2, y2):
        """
        Calculates the Chebyshev distance between [x1, y1] and [x2, y2]
        :param x1: row index of first state
        :param y1: column index of first state
        :param x2: row index of second state
        :param y2: column index of second state
        :return: the Chebyshev distance between the states.
        """
        return max(abs(x1 - x2), abs(y1 - y2))

    def is_adjacent_by_manhattan(self, row1, col1, row2, col2):
        """
        Determines whether two states are adjacent calculated by Manhattan distance.
        The are adjacent if the Manhattan distance is 1.
        :param row1: row index of first state
        :param col1: column index of first state
        :param row2: row index of second state
        :param col2: column index of second state
        :return: True if they are adjacent by Manhattan distance, False is they are not adjacent.
        """
        return self.manhattan_distance(row1, col1, row2, col2) == 1

    def is_adjacent_by_chebyshev(self, row1, col1, row2, col2):
        """
        Determines whether two states are adjacent calculated by Chebyshev distance.
        The are adjacent if the Chebyshev distance is 1.
        :param row1: row index of first state
        :param col1: column index of first state
        :param row2: row index of second state
        :param col2: column index of second state
        :return: True if they are adjacent by Chebyshev distance, False is they are not adjacent.
        """
        return self.chebyshev_distance(row1, col1, row2, col2) == 1

    def is_goal(self, row, col):
        """
        Determines whether a state at the given row and column is a goal state, that is, equals 'G'.
        :param row: row index
        :param col: column index
        :return: a boolean indicating whether the state is a goal state.
        """
        return self.maze[row][col] == 'G'

    def is_open(self, row, col):
        """
        Determines whether a state at the given row and column is open, that is, equals '_', 'S', or 'G'.
        :param row: row index
        :param col: column index
        :return: a boolean indicating whether the state is open.
        """
        value = self.maze[row][col]
        return value == '_' or value == 'S' or value == 'G'

    def is_blocked(self, row, col):
        """
        Determines whether a state at the given row and column is blocked, that is, equals 'X'.
        :param row: row index
        :param col: column index
        :return: a boolean indicating whether the state is blocked.
        """
        return self.maze[row][col] == 'X'

    def get_result_maze(self, path):
        """
        Modify the maze such that the path taken between start and goal state is marked by 'P'.
        :param path: a list of ordered lists containing states of the path.
        :return: The maze with the path taken marked by 'P'
        """
        # todo: remove basic error checks
        # do some basic error checking of the result path here
        # if not self.is_adjacent_by_chebyshev(path[0][0], path[0][1], self.start_pos[0], self.start_pos[1]):
        #     print('Error 1: Some error must have occurred.')
        # if not self.is_adjacent_by_chebyshev(path[len(path)-1][0], path[len(path)-1][1],
        #                                      self.goal_pos[0], self.goal_pos[1]):
        #     print('Error 2: Some error must have occurred.')
        # for i in range(len(path) - 1):
        #     if not self.is_adjacent_by_chebyshev(path[i][0], path[i][1], path[i+1][0], path[i+1][1]):
        #         print('Error 3: Some error must have occurred.')

        for position in path:
            self.maze[position[0]][position[1]] = 'P'
        return self.maze


def read_file(file_name):
    file = open(file_name, 'r')
    input_lines = [list(line.rstrip('\n')) for line in file]
    mazes = []
    maze = []
    for line in input_lines:
        if not line:
            mazes.append(maze)
            maze = []
        else:
            maze.append(line)
    if len(maze) > 0:
        mazes.append(maze)
    file.close()
    return mazes


def write_to_file(lis_2d, file_name):
    """
    Write the data to output file.
    :param lis_2d: a 2D list
    :param file_name: output file name
    """
    file = open(file_name, 'a+')
    for row in range(0, len(lis_2d)):
        # needed to add 1 to x because row and column numbers on a chess board
        # are 1 higher than Python list indices.
        new_line = ''.join(lis_2d[row])
        file.write(new_line + '\n')
    file.close()


def append_line_to_file(line, file_name):
    file = open(file_name, 'a+')
    file.write(line + '\n')
    file.close()


def print_list_2d(lis_2d):
    """
    Print out a 2D list in nice format.
    :param lis_2d: a 2D list
    """
    for lis in lis_2d:
        for item in lis:
            print(item, end='')
        print()
    print()


def print_list_3d(lis_3d):
    """
    Print out a 3D list in nice format.
    :param lis_3d: a 3D list
    """
    count = 0
    for lis_2d in lis_3d:
        print('Element in 3d list at position', count, end='.\n')
        for lis in lis_2d:
            for item in lis:
                print(item, end='')
            print()
        count += 1
    print()


def main():
    input_file_name_up_down = 'path_finding_a.txt'
    input_file_name_diagonal = 'path_finding_b.txt'
    output_file_name_up_down = 'path_finding_a_out.txt'
    output_file_name_diagonal = 'path_finding_b_out.txt'

    # open and then close the output file with w+ so that the file starts empty
    file = open(output_file_name_up_down, 'w+')
    file.close()
    file = open(output_file_name_diagonal, 'w+')
    file.close()

    input_mazes_up_down = read_file(input_file_name_up_down)
    num_input_mazes_up_down = len(input_mazes_up_down)
    if num_input_mazes_up_down == 0:
        print("No input mazes for agent to be allowed to only move up, down, left and right.")
    else:
        print("Finding solutions to mazes when allowed to move up, down, left and right.")
        for i in range(num_input_mazes_up_down):
            maze = input_mazes_up_down[i]
            path_finding_up_down = PathFinding(maze)
            print("Finding a solution for maze number", i, "with dimension", len(maze), "by", len(maze[0]))
            st = time.time()
            # call the algorithm to get path
            path_up_down_greedy = path_finding_up_down.greedy_search_up_down()
            # generate result maze from path
            result_maze = path_finding_up_down.get_result_maze(path_up_down_greedy)
            # write algorithm name to file
            append_line_to_file('Greedy', output_file_name_up_down)
            # write maze to file
            write_to_file(result_maze, output_file_name_up_down)
            print("    the time used for greedy algorithm is", time.time() - st)

            st = time.time()
            # call the algorithm to get path
            path_up_down_a_star = path_finding_up_down.a_star_search_up_down()
            # generate result maze from path
            result_maze = path_finding_up_down.get_result_maze(path_up_down_a_star)
            # write algorithm name to file
            append_line_to_file('A*', output_file_name_up_down)
            # write maze to file
            write_to_file(result_maze, output_file_name_up_down)
            append_line_to_file('', output_file_name_up_down)
            print("    the time used for A* algorithm is", time.time() - st)
    print()

    input_mazes_diagonal = read_file(input_file_name_diagonal)
    num_input_mazes_diagonal = len(input_mazes_diagonal)
    if num_input_mazes_diagonal == 0:
        print("No input maze fow agent to be allowed to also move diagonally.")
    else:
        print("Finding solutions to mazes when also allowed to move diagonally.")
        for i in range(num_input_mazes_diagonal):
            maze = input_mazes_diagonal[i]
            path_finding_diagonal = PathFinding(maze)
            print("Finding a solution for maze number", i, "with dimension", len(maze), "by", len(maze[0]))
            st = time.time()
            # call the algorithm to get path
            path_diagonal_greedy = path_finding_diagonal.greedy_search_diagonal()
            # generate result maze from path
            result_maze = path_finding_diagonal.get_result_maze(path_diagonal_greedy)
            # write algorithm name to file
            append_line_to_file('Greedy', output_file_name_diagonal)
            # write maze to file
            write_to_file(result_maze, output_file_name_diagonal)
            print("    the time used for greedy algorithm is", time.time() - st)

            st = time.time()
            # call the algorithm to get path
            path_diagonal_a_star = path_finding_diagonal.a_star_search_diagonal()
            # generate result maze from path
            result_maze = path_finding_diagonal.get_result_maze(path_diagonal_a_star)
            # write algorithm name to file
            append_line_to_file('A*', output_file_name_diagonal)
            # write maze to file
            write_to_file(result_maze, output_file_name_diagonal)
            append_line_to_file('', output_file_name_diagonal)
            print("    the time used for A* algorithm is", time.time() - st)


main()
