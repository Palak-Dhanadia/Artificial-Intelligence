from queue import PriorityQueue

class Node:
    def __init__(self, label, path_cost, parent):
        self.label = label
        self.path_cost = path_cost
        self.parent = parent

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __repr__(self):
        path = construct_path(self)
        return ('(%s, %s, %s)'
                % (repr(self.label), repr(self.path_cost), repr(path)))


def construct_path(node):
    """
    this method constructs the path as a list from the root to the node
    :param node: a Node object
    :return: list
    """
    path_from_root = [node.label]
    while node.parent:
        node = node.parent
        path_from_root = [node.label] + path_from_root
    return path_from_root


def remove_node_with_higher_cost(new_node, frontier):
    """
    this method removes the node from the priority queue if the new_node has a the same label but a lesser cost
    :param new_node: node
    :param frontier: priority queue
    :return: priority queue
    """
    removed = False
    frontier_list = frontier.queue
    for item in frontier_list:
        if item.label == new_node.label and item.path_cost > new_node.path_cost:
            removed_item = item
            frontier_list.remove(item)
            removed = True
            break

    if removed:
        new_queue = PriorityQueue()
        frontier_list.append(new_node)
        for item in frontier_list:
            new_queue.put(item)
        return new_queue
    else:
        return frontier


def in_frontier(new_node, frontier):
    """
    this method checks if the new_node.label is already present in the frontier
    :param new_node: node
    :param frontier: priority queue
    :return: boolean
    """
    frontier_list = frontier.queue
    for item in frontier_list:
        if item.label == new_node.label:
            return True
    return False


def usc(nxobject, initial, goal,):
    """
    this method performs the uniform cost search
    :param nxobject: the weighted networkx graph
    :param initial: the initial state or root
    :param goal: the goal state or the destination
    :return: a node with the optimal path
    """
    number_of_explored_nodes = 1
    node = Node(initial, 0, None)
    frontier = PriorityQueue()
    # initial state is added to priority queue
    frontier.put(node)
    explored = set()
    while not frontier.empty():
        # pop the first element from the priority queue
        node = frontier.get()
        # check if the node is in the goal state then return node
        if node.label == goal:
            print("Number of explorations = ", number_of_explored_nodes)
            return node
        # else add the node to the explored set
        number_of_explored_nodes += 1
        explored.add(node.label)
        # getting all the neighbours of the node
        neighbours = nxobject.neighbors(node.label)
        for child_label in neighbours:
            cost = nxobject.edges[(node.label, child_label)]['weight']
            child = Node(child_label, node.path_cost + cost, node)
            # check if the child node is already explored or not
            if child_label not in explored and not in_frontier(child, frontier):
                # add the child to the frontier
                frontier.put(child)
            # if the node already exists in the frontier with a higher cost, then replace it
            elif in_frontier(child, frontier):
                frontier = remove_node_with_higher_cost(child, frontier)