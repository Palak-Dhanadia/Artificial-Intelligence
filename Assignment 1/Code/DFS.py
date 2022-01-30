# Your function implementing DFS
def construct_path_from_root(node, root):
    """the non-recursive way!"""

    path_from_root = [node['label']]
    while node['parent']:
        node = node['parent']
        path_from_root = [node['label']] + path_from_root
    return path_from_root


def dfs(nxobject, initial, goal, compute_exploration_cost=False, reverse=False):
    """the no-oop way!"""

    frontier = [{'label': initial, 'parent': None}]
    explored = {initial}
    number_of_explored_nodes = 1

    while frontier:
        node = frontier.pop()  # pop from the right of the list
        number_of_explored_nodes += 1
        if node['label'] == goal:
            if compute_exploration_cost:
                print('number of explorations = {}'.format(number_of_explored_nodes))
            return node

        neighbours = reversed(list(nxobject.neighbors(node['label']))) if reverse else nxobject.neighbors(node['label'])
        for child_label in neighbours:

            child = {'label': child_label, 'parent': node}
            if child_label not in explored:
                frontier.append(child)  # added to the right of the list, so it is a LIFO
                explored.add(child_label)

    return None