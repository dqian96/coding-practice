# Problem: Longest Path Labelled Tree

"""

You're given a tree with nodes 1-N. Each node n is labelled with some integer A[n-1].
An edge exists between two nodes E[i] and E[i+1] for all i E [0, len(E)), i % 2 == 0.

Determine the longest path in the tree such that all nodes on the path have the same label.

i.e. A = [1, 1, 1, 2, 2] and E = [1, 2, 1, 3, 2, 4, 5] returns 2

Solution: Create a graph of N nodes using the given information. However, there is only an edge
between nodes if the edge is given AND the nodes have the same label. This is because
we do not consider paths/edges between nodes with different labels.

The graph is basically several connected components. Each connected component has nodes
of the same label.

Do DFS on the entire graph to find the largest connected component. Since the graph is a tree,
the longest path = # nodes in the largest connected component - 1

"""

from collections import defaultdict

def find_num_nodes(graph, node, visited):
    visited.add(node)
    num_nodes = 1
    for neighbour in graph[node]:
        if neighbour in visited:
            continue
        num_nodes += find_num_nodes(graph, neighbour, visited)
    return num_nodes

def solution(A, E):
    # create graph
    graph = defaultdict(list)

    for i in range(0, len(E), 2):
        n1 = E[i]
        n2 = E[i + 1]
        if A[n1 - 1] == A[n2 - 1]:
            # make an edge iff same label
            graph[n1].append(n2)
            graph[n2].append(n1)

    # find largest connected component
    visited = set()
    largest_connected_component = 0
    for node in range(1, len(A) + 1):
        if node in visited:
            continue
        largest_connected_component = max(largest_connected_component, find_num_nodes(graph, node, visited))
    
    return 0 if largest_connected_component == 0 else largest_connected_component - 1      # since cc is a tree, there will be one less edge than nodes
