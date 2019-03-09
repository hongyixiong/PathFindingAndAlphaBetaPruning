def read_input(file_name):
    # todo: last string splitted has '\n' at the end
    # todo: cannot deal with mutiple lines, must be single line
    file = open(file_name, 'r')
    for line in file:
        input_list = line.split(' ')
    return input_list


def main():
    input_file_name = 'alphabeta.txt'
    input_data_in_string = read_input(input_file_name)