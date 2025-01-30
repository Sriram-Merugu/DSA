Graph = {
    0: set([1, 2, 3]),
    1: set([0, 4]),
    2: set([0, 4]),
    3: set([0, 4]),
    4: set([1, 2, 3])
}


def dfs(graph, node, visited):
    if visited is None:
        visited = set()
    visited.add(node)
    if len(visited) != len(graph):
        print(f"{node} -> ", end='')
    else:
        print(node)
    for adj_node in graph[node]:
        if adj_node not in visited:
            dfs(graph, adj_node, visited)


print("DFS traversal for the graph is: ")
dfs(Graph, 0, visited=None)
