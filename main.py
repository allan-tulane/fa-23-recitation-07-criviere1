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
    while len(frontier) != 0:
        ###TODO
        n = frontier.pop()
        result.add(n)
        for i in graph[n]: # only want to visit once so if already in frontier list, don't add
            if i not in result:
                frontier.add(i)
    return result



def connected(graph):
    ### TODO
    n = len(graph)
    # reachable should return every node if it is a connected graph
    # so the length of what reachable returns should be the length of the graph
    r = len(reachable(graph, list(graph.keys())[0]))
    if n == r:
        return True
    else:
        return False


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    r = []
    frontier = set(list(graph.keys())) # all the nodes in the graph
    while len(frontier) != 0:
        n = frontier.pop()
        reach = reachable(graph, n)
        frontier = frontier - reach
        r.append(reach)


    return len(r)
