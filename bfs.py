from queue import PriorityQueue

# no.of vertices
v = 6

# Declaring the graph
graph = [[] for i in range(v)]


def best_first_search(src, des, n):
    visited = [False] * n

    # Declaring Priority Queue
    pq = PriorityQueue()

    pq.put((0, src))  # cost, vertex as it should be in cost priority
    visited[src] = True

    while pq:
        u = pq.get()[1]  # removes left most element in pq, (as it in order of cost) and node element gets assigned to u

        print(u, end=" ")

        if u == des:  # If target is found, then exit the loop
            break

        print('-->', end=" ")

        for node, cost in graph[u]:
            if not visited[node]:
                visited[node] = True
                pq.put((cost, node))


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

source = 0
destination = 5

best_first_search(source, destination, v)
