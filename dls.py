Graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Path to find the goal node
p = []


# depth limit search
def dls(graph, node, visited, limit, goal, path):
    global p
    if visited is None:
        visited = set()
        path.append(node)

    if node == goal:
        p = path[:]
        return True
    visited.add(node)
    if limit > 1:
        for adj_node in graph[node]:
            if adj_node not in visited:
                dls(graph, adj_node, visited, limit - 1, goal, path + [adj_node])


limit = 3
visited = None
goal = 'F'
start = 'A'

print("DFS traversal for the graph is: ")
dls(Graph, start, visited, limit, goal, [])
if p:
    print(f"Node {start} is found in the limit {limit}")
    print("The path is: ")
    print('->'.join(p))
else:
    print(f"Node {start} is not found in the limit {limit}")