import sys

def prim(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    selected[0] = True  # 从第一个顶点开始
    mst_edges = []
    total_weight = 0

    for _ in range(num_vertices - 1):
        min_edge = (None, None, float('inf'))
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j] < min_edge[2]:
                        min_edge = (i, j, graph[i][j])
        
        selected[min_edge[1]] = True
        mst_edges.append((min_edge[0], min_edge[1], min_edge[2]))
        total_weight += min_edge[2]

    return total_weight, mst_edges

def main():
    INF = float('inf')
    graph = [
        [0, 12, INF, INF, INF, 16, 14],
        [12, 0, 10, INF, INF, 7, INF],
        [INF, 10, 0, 3, 5, 6, INF],
        [INF, INF, 3, 0, 4, INF, INF],
        [INF, INF, 5, 4, 0, 2, 8],
        [16, 7, 6, INF, 2, 0, 9],
        [14, INF, INF, INF, 8, 9, 0]
    ]
    
    total_weight, mst_edges = prim(graph)
    
    print(f"PRIM(A)={total_weight}: ", end="")
    for u, v, weight in mst_edges:
        print(chr(u + ord('A')), end=" ")
    print()

main()
print('许会杰','2125120073')
