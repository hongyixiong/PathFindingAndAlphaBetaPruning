import copy
import heapq
import time


class PathFinding:
    def __init__(self, maze):
        self.maze = maze
        self.start_state = None  # represented by an ordered pair (x, y) as a tuple
        self.goal_state = None
        self.initialize_start_goal_states()

    def initialize_start_goal_states(self):
        """
        Finds the location of start and goal states of the maze, represented by ordered lists
        consisting of row and column positions, that is, [a, b] represents a state at row a and column b.
        Sets the start and goal states of self.
        """
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                state = (i, j)
                if self.maze[i][j] == 'S':
                    self.start_state = state
                elif self.is_goal(state):
                    self.goal_state = state

    def greedy_search_up_down(self):
        """
        Find the path from start to goal using greedy search in a maze where you can only move up, down, left, or right.
        The path is represented by a map from states to its previous state.
        Example: if came_from[(x_1, y_1)] = (x_2, y_2) and came_from[(x_2, y_2)] = (x_3, y_3),
                 then the path should be [(x_3, y_3), (x_2, y_2), x_1, y_1)]
        :return: a map from state to which state it came from.
        """
        frontier = []
        heapq.heappush(frontier, (0, self.start_state))
        came_from = dict()
        came_from[self.start_state] = None

        while len(frontier) > 0:
            current = heapq.heappop(frontier)
            current_state = current[1]
            if self.is_goal(current_state):
                break
            for next_state in self.get_open_neighbours_up_down(current_state):
                if next_state not in came_from:
                    priority = self.manhattan_heuristic(next_state)
                    heapq.heappush(frontier, (priority, next_state))
                    came_from[next_state] = current_state
        return came_from

    def a_star_search_up_down(self):
        """
        Find the path from start to goal using A* search in a maze where you can only move up, down, left, or right.
        The path is represented by a map from states to its previous state.
        Example: if came_from[(x_1, y_1)] = (x_2, y_2) and came_from[(x_2, y_2)] = (x_3, y_3),
                 then the path should be [(x_3, y_3), (x_2, y_2), x_1, y_1)]
        :return: a map from state to which state it came from.
        """
        frontier = []
        heapq.heappush(frontier, (0, self.start_state))
        came_from = dict()
        cost_so_far = dict()
        came_from[self.start_state] = None
        cost_so_far[self.start_state] = 0

        while len(frontier) > 0:
            current = heapq.heappop(frontier)
            current_state = current[1]
            if self.is_goal(current_state):
                break
            for next_state in self.get_open_neighbours_up_down(current_state):
                new_cost = cost_so_far[current_state] + 1
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = new_cost + self.manhattan_heuristic(next_state)
                    heapq.heappush(frontier, (priority, next_state))
                    came_from[next_state] = current_state
        return came_from

    def greedy_search_diagonal(self):
        """
        Find the path from start to goal using greedy search in a maze where you can also move diagonally.
        The path is represented by a map from states to its previous state.
        Example: if came_from[(x_1, y_1)] = (x_2, y_2) and came_from[(x_2, y_2)] = (x_3, y_3),
                 then the path should be [(x_3, y_3), (x_2, y_2), x_1, y_1)]
        :return: a map from state to which state it came from.
        """
        frontier = []
        heapq.heappush(frontier, (0, self.start_state))
        came_from = dict()
        came_from[self.start_state] = None

        while len(frontier) > 0:
            current = heapq.heappop(frontier)
            current_state = current[1]
            if self.is_goal(current_state):
                break
            for next_state in self.get_open_neighbours_diagonal(current_state):
                # print('ck1', current, next_state)
                if next_state not in came_from:
                    priority = self.chebyshev_heuristic(next_state)
                    # print('ck2: priority for next_state', priority)
                    heapq.heappush(frontier, (priority, next_state))
                    came_from[next_state] = current_state
        return came_from

    def a_star_search_diagonal(self):
        """
        Find the path from start to goal using A* search in a maze where you can also move diagonally.
        The path is represented by a map from states to their previous state.
        Example: if came_from[(x_1, y_1)] = (x_2, y_2) and came_from[(x_2, y_2)] = (x_3, y_3),
                 then the path should be [(x_3, y_3), (x_2, y_2), x_1, y_1)]
        :return: a map from states to their previous state
        """
        frontier = []
        heapq.heappush(frontier, (0, self.start_state))
        came_from = dict()
        cost_so_far = dict()
        came_from[self.start_state] = None
        cost_so_far[self.start_state] = 0

        while len(frontier) > 0:
            current = heapq.heappop(frontier)
            current_state = current[1]
            if self.is_goal(current_state):
                break
            for next_state in self.get_open_neighbours_diagonal(current_state):
                new_cost = cost_so_far[current_state] + 1
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = new_cost + self.chebyshev_heuristic(next_state)
                    heapq.heappush(frontier, (priority, next_state))
                    came_from[next_state] = current_state
        return came_from

    def manhattan_heuristic(self, state):
        """
        Calculates the Manhattan heuristic at the state (x, y).
        This is the Manhattan distance between the given state and the goal state.

        :param state: an ordered pair as a tuple (x, y)
        :return: a value representing the Manhattan heuristic of the given state.
        """
        return self.manhattan_distance(state, self.goal_state)

    def manhattan_distance(self, state_1, state_2):
        """
        Calculates the Manhattan distance between state_1 (x1, y1) and state_2 (x2, y2)

        :param state_1: first ordered pair in the form (x1, y1)
        :param state_2: second ordered pair in the form (x2, y2)
        :return: the Manhattan distance between the states.
        """
        return abs(state_1[0] - state_2[0]) + abs(state_1[1] - state_2[1])

    def chebyshev_heuristic(self, state):
        """
        Calculates the Chebyshev heuristic at the state (x, y).
        This is the Chebyshev distance between the given state and the goal state.

        :param state: an ordered pair as a tuple (x, y)
        :return: the value of the Chebyshev heuristic of at given state.
        """
        return self.chebyshev_distance(state, self.goal_state)

    def chebyshev_distance(self, state_1, state_2):
        """
        Calculates the Chebyshev distance between state_1 (x1, y1) and state_2 (x2, y2)

        :param state_1: first ordered pair in the form (x1, y1)
        :param state_2: second ordered pair in the form (x2, y2)
        :return: the Chebyshev distance between the states.
        """
        return max(abs(state_1[0] - state_2[0]), abs(state_1[1] - state_2[1]))

    def get_open_neighbours_up_down(self, state):
        """
        Find open neighbours for the state.
        A neighbours is a state that is in the direction up, down, left or right of the given state.
        :return: a list of open neighbors for state point
        """
        # todo: maybe need to check boundaries, if there is no wall around the state.
        row = state[0]
        col = state[1]
        neighbours = [(row - 1, col),  # left
                      (row + 1, col),  # right
                      (row, col - 1),  # up
                      (row, col + 1)]  # down

        return list(filter(lambda neighbour: self.is_open(neighbour), neighbours))

    def get_open_neighbours_diagonal(self, state):
        """
        Find open neighbors for the state state.
        A neighbours is a state that is in the direction up, down, left or right or diagonally adjacent of the given state.
        :return: a list of open neighbors for state point
        """
        # todo: maybe need to check boundaries, if there is no wall around the state.
        row = state[0]
        col = state[1]
        neighbours = [(row - 1, col),  # left
                      (row + 1, col),  # right
                      (row, col - 1),  # up
                      (row, col + 1),  # down
                      (row - 1, col - 1),  # top left
                      (row - 1, col + 1),  # top right
                      (row + 1, col - 1),  # bottom left
                      (row + 1, col + 1)]  # bottom right

        return list(filter(lambda neighbour: self.is_open(neighbour), neighbours))

    def is_adjacent_by_manhattan(self, state_1, state_2):
        """
        Determines whether two states are adjacent calculated by Manhattan distance.
        The are adjacent if the Manhattan distance is 1.

        :param state_1: first ordered pair in the form (x1, y1)
        :param state_2: second ordered pair in the form (x2, y2)
        :return: True if they are adjacent by Manhattan distance, False is they are not adjacent.
        """
        return self.manhattan_distance(state_1, state_2) == 1

    def is_adjacent_by_chebyshev(self, state_1, state_2):
        """
        Determines whether two states are adjacent calculated by Chebyshev distance.
        The are adjacent if the Chebyshev distance is 1.

        :param state_1: first ordered pair in the form (x1, y1)
        :param state_2: second ordered pair in the form (x2, y2)
        :return: True if they are adjacent by Chebyshev distance, False is they are not adjacent.
        """
        return self.chebyshev_distance(state_1, state_2) == 1

    def is_goal(self, state):
        """
        Determines whether a state at the given row and column is a goal state, that is, equals 'G'.
        :param state: an ordered pair as a tuple (x, y) representing the position
        :return: a boolean indicating whether the state is a goal state.
        """
        return self.maze[state[0]][state[1]] == 'G'

    def is_open(self, state):
        """
        Determines whether a state at the given row and column is open, that is, equals '_', 'S', or 'G'.
        :param state: an ordered pair as a tuple (x, y) representing the position
        :return: a boolean indicating whether the state is open.
        """
        value = self.maze[state[0]][state[1]]
        return value == '_' or value == 'S' or value == 'G'

    def is_blocked(self, state):
        """
        Determines whether a state at the given row and column is blocked, that is, equals 'X'.
        :param state: an ordered pair as a tuple (x, y) representing the position
        :return: a boolean indicating whether the state is blocked.
        """
        return self.maze[state[0]][state[1]] == 'X'

    def get_result_maze(self, path_map):
        """
        Modify the maze such that the path taken between start and goal state is marked by 'P'.
        :param path_map: a map from states to their previous state
        :return: The maze with the path taken marked by 'P'
        """
        current_state = self.goal_state
        while current_state != self.start_state:
            if current_state in path_map:
                previous_state = path_map[current_state]
                self.maze[previous_state[0]][previous_state[1]] = 'P'
                current_state = previous_state
            else:
                print('Error 01: unexpected error after all algorithms are correctly implemented.')
                break
        # set the start state back to 'S' since it was set to 'P' when reconstructing path.
        self.maze[self.start_state[0]][self.start_state[1]] = 'S'
        return self.maze


def read_file(file_name):
    # todo: error when leading line is blank
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
            m = len(maze)
            n = len(maze[0])
            print("Finding a solution for maze number", i, "with dimension", m, "by", n)
            path_finding_up_down_greedy = PathFinding(copy.deepcopy(maze))
            st = time.time()
            # call the algorithm to get path
            path_up_down_greedy = path_finding_up_down_greedy.greedy_search_up_down()
            # generate result maze from path
            result_maze = path_finding_up_down_greedy.get_result_maze(path_up_down_greedy)
            # write algorithm name to file
            append_line_to_file('Greedy', output_file_name_up_down)
            # write maze to file
            write_to_file(result_maze, output_file_name_up_down)
            print("    the time used for greedy algorithm is", time.time() - st)

            path_finding_up_down_a_star = PathFinding(copy.deepcopy(maze))
            st = time.time()
            # call the algorithm to get path
            path_up_down_a_star = path_finding_up_down_a_star.a_star_search_up_down()
            # generate result maze from path
            result_maze = path_finding_up_down_a_star.get_result_maze(path_up_down_a_star)
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
            m = len(maze)
            n = len(maze[0])
            print("Finding a solution for maze number", i, "with dimension", m, "by", n)
            path_finding_diagonal_greedy = PathFinding(copy.deepcopy(maze))
            st = time.time()
            # call the algorithm to get path
            path_diagonal_greedy = path_finding_diagonal_greedy.greedy_search_diagonal()
            # generate result maze from path
            result_maze = path_finding_diagonal_greedy.get_result_maze(path_diagonal_greedy)
            # write algorithm name to file
            append_line_to_file('Greedy', output_file_name_diagonal)
            # write maze to file
            write_to_file(result_maze, output_file_name_diagonal)
            print("    the time used for greedy algorithm is", time.time() - st)

            # todo: find out why it doesn't work if shallow copied
            path_finding_diagonal_a_star = PathFinding(copy.deepcopy(maze))
            st = time.time()
            # call the algorithm to get path
            path_diagonal_a_star = path_finding_diagonal_a_star.a_star_search_diagonal()
            # generate result maze from path
            result_maze = path_finding_diagonal_a_star.get_result_maze(path_diagonal_a_star)
            # write algorithm name to file
            append_line_to_file('A*', output_file_name_diagonal)
            # write maze to file
            write_to_file(result_maze, output_file_name_diagonal)
            append_line_to_file('', output_file_name_diagonal)
            print("    the time used for A* algorithm is", time.time() - st)


main()
