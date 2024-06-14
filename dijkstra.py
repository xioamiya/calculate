import heapq

def dijkstra(graph, start):
    num_vertices = len(graph)
    dist = [float('inf')] * num_vertices
    dist[start] = 0
    priority_queue = [(0, start)]
    visited = [False] * num_vertices

    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        if visited[u]:
            continue
        visited[u] = True

        for v in range(num_vertices):
            if graph[u][v] != float('inf') and not visited[v]:
                new_dist = current_dist + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(priority_queue, (new_dist, v))

    return dist

def print_distances(dist, start):
    vertex_labels = ['A', 'B', 'C', 'D', 'E', 'F']
    start_label = vertex_labels[start]
    
    print(f"dijkstra({start_label}):")
    for i, d in enumerate(dist):
        if d == float('inf'):
            print(f"  shortest({start_label}, {vertex_labels[i]})=INF")
        else:
            print(f"  shortest({start_label}, {vertex_labels[i]})={d}")

def main():
    INF = float('inf')
    graph = [
        [0, 2, 5, INF, INF, INF],
        [INF, 0, 1, 3, INF, INF],
        [INF, INF, 0, 3, 4, 1],
        [INF, INF, INF, 0, 1, 4],
        [INF, INF, INF, INF, 0, 1],
        [INF, INF, INF, INF, INF, 0]
    ]
    
    start_vertex = 0  # Start from vertex 'A'
    dist = dijkstra(graph, start_vertex)
    print_distances(dist, start_vertex)

main()
print('许会杰','2125120073')
