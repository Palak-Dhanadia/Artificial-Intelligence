
def bfs(nxobject, initial, goal, compute_exploration_cost=False, reverse=False):
    if initial == goal:  # just in case, because now we are checking the children
        return None

    number_of_explored_nodes = 1
    frontier = [{'label': initial, 'parent': None}]
    # FIFO queue should NOT be implemented with a list, this is slow! better to use deque
    explored = {initial}

    while frontier:
        node = frontier.pop()  # pop from the right of the list

        neighbours = reversed(list(nxobject.neighbors(node['label']))) if reverse else nxobject.neighbors(node['label'])

        for child_label in neighbours:
            child = {'label': child_label, 'parent': node}
            if child_label == goal:
                if compute_exploration_cost:
                    print('number of explorations = {}'.format(number_of_explored_nodes))
                return child

            if child_label not in explored:
                frontier = [child] + frontier  # added to the left of the list, so a FIFO!
                number_of_explored_nodes += 1
                explored.add(child_label)

    return None

