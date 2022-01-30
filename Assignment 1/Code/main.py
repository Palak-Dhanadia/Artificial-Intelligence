from tube import compute_path_cost
from tube import loaddata
from USC import usc
from USC import construct_path
from DFS import construct_path_from_root
from DFS import dfs
from BFS import bfs
from Heuristic import heuristic

print("Select Search Algorithm")
print("1.DFS")
print("2.BFS")
print("3.UCS")
print("4.Heuristics")


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the three options
    if choice in ('1', '2', '3'):
        start_station = input("Enter Starting Station:")
        dest_station = input("Enter Destination Station:")

        if choice == '1':
            solution = dfs(loaddata(), start_station, dest_station, True)
            path = construct_path_from_root(solution, start_station)
            path_cost = compute_path_cost(loaddata(), path)
            print("Total cost: ", path_cost)
            print('Path:', path)
            print('Number of nodes:', len(path))

        elif choice == '2':
            solution = bfs(loaddata(), start_station, dest_station, True)
            path = construct_path_from_root(solution, start_station)
            path_cost = compute_path_cost(loaddata(), path)
            print("Total cost: ", path_cost)
            print('Path:', path)
            print('Number of nodes:', len(path))

        elif choice == '3':
            solution = usc(loaddata(), start_station, dest_station)
            print("Total cost: ", solution.path_cost)
            print("Path:", construct_path(solution))
            print('Number of nodes:', len(construct_path(solution)))

        elif choice == '4':
            solution = heuristic(loaddata(), start_station, dest_station)
            print("Total cost: ", solution)
            print("Path:", construct_path_from_root(solution, None))



        # break the while loop if answer is no
        next_search = input("Let's do next search? (yes/no): ")
        if next_search == "no":
            break

    else:
        print("Invalid Input")
        break



