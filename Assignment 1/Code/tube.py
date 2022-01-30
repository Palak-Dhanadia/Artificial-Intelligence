import csv
import matplotlib.pyplot as plt
import networkx as nx


def loaddata():
    """this method loads the csv file to the networkx object
    :return: networkx object"""
    with open('tubedata.csv') as tubedata_file:
        G = nx.Graph()
        tubedata = csv.reader(tubedata_file, skipinitialspace=True)
        for row in tubedata:
            #print(row)
            G.add_edge(row[0], row[1], weight=float(row[3]))
            #print(G.number_of_nodes())
            #print(G.number_of_edges())
    return G


def show_weighted_graph(networkx_graph, node_size, font_size, fig_size):
  # Allocate the given fig_size in order to have space for each node
  plt.figure(num=None, figsize=fig_size, dpi=80)
  plt.axis('off')
  # Compute the position of each vertex in order to display it nicely
  nodes_position = nx.spring_layout(networkx_graph)
  # You can change the different layouts depending on your graph
  # Extract the weights corresponding to each edge in the graph
  edges_weights  = nx.get_edge_attributes(networkx_graph,'weight')
  # Draw the nodes (you can change the color)
  nx.draw_networkx_nodes(networkx_graph, nodes_position, node_size=node_size,
                         node_color = ["red"]*networkx_graph.number_of_nodes())
  # Draw only the edges
  nx.draw_networkx_edges(networkx_graph, nodes_position,
                         edgelist=list(networkx_graph.edges), width=2)
  # Add the weights
  nx.draw_networkx_edge_labels(networkx_graph, nodes_position,
                               edge_labels = edges_weights)
  # Add the labels of the nodes
  nx.draw_networkx_labels(networkx_graph, nodes_position, font_size=font_size,
                          font_family='sans-serif')
  plt.axis('off')
  plt.show()

show_weighted_graph(loaddata(), 500, 10, (35,35))

def compute_path_cost(nxobject, path):
  """
    Compute cost of a path
  """
  cost = 0
  for index_station in range(len(path) - 1):
    cost += nxobject[path[index_station]][path[index_station + 1]]["weight"]
  return cost
