import random


def print_maze(maze):
    for m in maze:
        print(''.join(map(str, m)))
    print()


def create_maze(m, n, blocked_probability):
    maze = [['X' for x in range(n)] for y in range(m)]

    start_x = random.randint(1, m - 2)
    start_y = random.randint(1, n - 2)
    goal_x = random.randint(1, m - 2)
    goal_y = random.randint(1, n - 2)

    while goal_x == start_x and goal_y == start_y:
        goal_x, goal_y = random.randint(1, m - 2), random.randint(1, n - 2)

    maze[start_x][start_y] = 'S'
    maze[goal_x][goal_y] = 'G'

    for x in range(m):
        for y in range(n):
            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                maze[x][y] = "X"
            else:
                num = random.random()
                if num < blocked_probability:
                    maze[x][y] = 'X'
                else:
                    maze[x][y] = '_'
                if x == start_x and y == start_y:
                    maze[x][y] = "S"
                if x == goal_x and y == goal_y:
                    maze[x][y] = "G"
    return maze


def append_line_to_file(line, file_name):
    file = open(file_name, 'a+')
    file.write(line + '\n')
    file.close()


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


def write_new_maze_to_input_files(m, n, blocked_probability):
    input_file_name_up_down = 'path_finding_a.txt'
    input_file_name_diagonal = 'path_finding_b.txt'
    empty_string = ''

    maze = create_maze(m, n, blocked_probability)
    append_line_to_file(empty_string, input_file_name_up_down)
    write_to_file(maze, input_file_name_up_down)
    append_line_to_file(empty_string, input_file_name_diagonal)
    write_to_file(maze, input_file_name_diagonal)


def clear_content_of_file(file_name):
    file = open(file_name, 'w+')
    file.close()


def main():
    input_file_name_up_down = 'path_finding_a.txt'
    input_file_name_diagonal = 'path_finding_b.txt'
    output_file_name_up_down = 'path_finding_a_out.txt'
    output_file_name_diagonal = 'path_finding_b_out.txt'

    # The following two lines is for clearing existing mazes in input files.
    # Comment out the following two lines out if you want to append a new maze.
    clear_content_of_file(input_file_name_up_down)
    clear_content_of_file(input_file_name_diagonal)

    # write a new maze into input file to be run by pathfinding.py.
    blocked_probability = 0.3
    num_row = 20
    num_col = 30
    write_new_maze_to_input_files(num_row, num_col, blocked_probability)


main()
# the following line when not commented will run the pathfinding.py
# import pathfinding
