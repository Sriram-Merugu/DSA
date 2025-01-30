from queue import PriorityQueue

# no.of vertices
v = 6

# Declaring the graph
graph = [[] for i in range(v)]

def best_first_search(src, des, pq):
    global v
    pq.put((0, src))  # heuristic_function, vertex as it should be in cost priority
    parent = [-1] * v  # To keep track of the parent node for each vertex
    visited = [False] * v
    visited[src] = True

    while not pq.empty():
        c, u = pq.get()

        if u == des:
            # Reconstruct the path from the parent array
            path = []
            while u != -1:
                path.insert(0, u)
                u = parent[u]
            return path

        for v, cost in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                pq.put((heuristic_function[v] + cost, v))

    return None

# Adding edge to the graph
def add_edge(x, y, cost):
    graph[x].append([y, cost])
    graph[y].append([x, cost])

add_edge(0, 1, 5)
add_edge(0, 2, 7)
add_edge(1, 3, 6)
add_edge(1, 4, 2)
add_edge(2, 4, 3)
add_edge(3, 5, 10)
add_edge(4, 5, 2)

heuristic_function = {
    0: 3,
    1: 5,
    2: 4,
    3: 6,
    4: 7,
    5: 8
}

source = 2
destination = 5

# Make heuristic_function as 0 for the destination
heuristic_function[destination] = 0

pq = PriorityQueue()
path = best_first_search(source, destination, pq)

if path:
    print("Path:", ' -> '.join(map(str, path)))
else:
    print("No path found.")
