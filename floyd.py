import numpy as np

def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = np.array(graph, dtype=float)
    
    # 初始化距离矩阵，INF表示无穷大
    INF = float('inf')
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and dist[i][j] == 0:
                dist[i][j] = INF
    
    # Floyd-Warshall算法
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def print_distance_matrix(dist):
    num_vertices = len(dist)
    vertex_labels = ['A', 'B', 'C']
    
    print("Floyd-Warshall Distance Matrix:")
    print("   ", end="")
    for label in vertex_labels:
        print(f"{label:>3}", end=" ")
    print()
    
    for i in range(num_vertices):
        print(f"{vertex_labels[i]:>2}:", end=" ")
        for j in range(num_vertices):
            if dist[i][j] == float('inf'):
                print("INF", end=" ")
            else:
                print(f"{dist[i][j]:>3}", end=" ")
        print()

def main():
    INF = float('inf')
    graph = [
        [0, 6, 13],
        [10, 0, 4],
        [5, INF, 0]
    ]
    
    dist = floyd_warshall(graph)
    print_distance_matrix(dist)

main()
print('许会杰','2125120073')