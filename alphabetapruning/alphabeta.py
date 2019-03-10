from collections import deque
nodes_examined = 0

class GraphNode:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return '{}, {}'.format(self.name, self.type)

# returns a list of list
def read_input(file_name):
    file = open(file_name, 'r')
    input_list = []
    curr_list = []
    curr_tup = ["", ""]
    # keep track of if we are currently reading the name of a node
    name_node = False
    # keep track of if we are currently reading the value of a node
    val_node = False
    for line in file:
        for ch in line:
            # reached end of the set
            if ch == "}":
                input_list.append(curr_list)
                curr_list = []
            # reached the name of a node
            elif ch.isalnum() or ch == "-":
                # if we are currently reading the name of a node, add to the node
                if name_node:
                    curr_tup[0] += ch
                # if we are currently reading the value, add to the value
                elif val_node:
                    curr_tup[1] += ch
                # else we start reading the name of the node
                else:
                    name_node = True
                    curr_tup[0] += ch
            elif ch == ",":
                # if we have finished reading the name of the node
                if name_node:
                    name_node = False
                    val_node = True
            elif ch == ")":
                val_node = False
                # add this tupple to the set
                curr_list.append(tuple(curr_tup))
                curr_tup = ["", ""]
            # else ignore whitespace and opening brackets
    return input_list


# nodes and edges are both a list of tuples
def create_graph(nodes, edges):
    # graphnodes is a dictionary in the format nodes[x] = y where
    # x is the name of the node and y is the node itself
    graphnodes = {}

    # construct the GraphNodes
    for node in nodes:
        # node[0] is the name of the node, node[1] is the type of the node
        newnode = GraphNode(node[0], node[1])
        graphnodes[newnode.name] = newnode

    # construct graph
    for n1, n2 in edges:
        if n2.isalpha():
            # add n2 as a child of n1
            graphnodes[n1].add_child(graphnodes[n2])
        else:
            graphnodes[n1].add_child(int(n2))
    # return the head of the graph
    return graphnodes[nodes[0][0]]


def print_tree(tree):
    # BFS through tree to print
    queue = deque()
    queue.append(tree)
    queue.append("#")
    while queue:
        node = queue.popleft()
        if node == "#":
            print('')
            if queue:
                queue.append("#")
        else:
            print(node, end='  |  ')
            if type(node) != int:
                for child in node.children:
                    queue.append(child)

def alpha_beta(current_node, alpha, beta):
    global nodes_examined
    if type(current_node) == int:
        nodes_examined += 1
        return current_node
    elif current_node.type == "MAX":
        for child in current_node.children:
            alpha = max(alpha, alpha_beta(child, alpha, beta))
            if alpha >= beta:
                break
        return alpha
    elif current_node.type == "MIN":
        for child in current_node.children:
            beta = min(beta, alpha_beta(child, alpha, beta))
            if beta <= alpha:
                break
        return beta




def main():
    global nodes_examined
    input_file_name = 'alphabeta.txt'
    input_data_in_string = read_input(input_file_name)
    print(input_data_in_string)
    i = 0
    graph_list = []
    while i < len(input_data_in_string):
        nodes_examined = 0
        # Every two lists in input_data_in_string consists of: list of nodes, list of edges
        graph = create_graph(input_data_in_string[i], input_data_in_string[i+1])
        i += 2
        print_tree(graph)
        graph_list.append(graph)
        score = alpha_beta(graph, float('-inf'), float('inf'))
        print(score, nodes_examined)


main()
