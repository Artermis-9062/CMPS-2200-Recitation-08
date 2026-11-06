"""
Name: Chuong Hoang Pham
"""

from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    vistited = set()
    while len(frontier) != 0:
        ###TODO
        node = frontier.pop() # Take node from frontier
        result.update(graph[node]) # Update all its neighbor
        if node not in vistited: # If haven't checked
            frontier.update(graph[node])
        vistited.add(node) # Add to visited
    return result
def connected(graph):
    ### TODO
    list_of_keys = list(graph.keys())
    start_node = list_of_keys[0]
    return len(reachable(graph, start_node)) == len(graph)
    pass

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO 
    unvisited_node = set(graph.keys())
    iter_set = iter(unvisited_node)
    visited = set([])
    count = 0
    while len(visited) != len(unvisited_node):
        curr_node = next(iter_set)
        if curr_node not in visited:
            visited.update(reachable(graph, curr_node))
            count += 1
    return count
