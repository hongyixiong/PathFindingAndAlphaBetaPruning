class GraphNode:
    def __init__(self, name):
        self.name = name
        self.children = set()

    def addChild(self, child):
        self.children.add(child)


# create a list of sets
def read_input(file_name):
    # todo: last string splitted has '\n' at the end
    # todo: cannot deal with mutiple lines, must be single line
    file = open(file_name, 'r')
    input_list = []
    currSet = set()
    currTup = ["",""]
    # keep track of if we are currently reading the name of a node
    nameNode = False
    # keep track of if we are currently reading the value of a node
    valNode = False
    for line in file:
        for ch in line:
            # reached end of the set
            if ch == "}":
                input_list.append(currSet)
                currSet = set()
            # reached the name of a node
            elif ch.isalnum():
                # if we are currently reading the name of a node, add to the node
                if nameNode:
                    currTup[0] += ch
                # if we are currently reading the value, add to the value
                elif valNode:
                    currTup[1] += ch
                # else we start reading the name of the node
                else:
                    nameNode = True
                    currTup[0] += ch
            elif ch == ",":
                # if we have finished reading the name of the node
                if nameNode == True:
                    nameNode = False
                    valNode = True
            elif ch == ")":
                valNode = False
                # add this tupple to the set
                currSet.add(tuple(currTup))
                currTup = ["",""]
            # else ignore whitespace and opening brackets
    return input_list



def main():
    input_file_name = 'alphabeta.txt'
    input_data_in_string = read_input(input_file_name)
    print(input_data_in_string)

main()