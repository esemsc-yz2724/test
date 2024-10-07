# floyd_warshall.py

def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.
    
    :param graph: 2D list representing the adjacency matrix of the graph
    :return: 2D list representing the shortest path distances between each pair of vertices
    """
    num_vertices = len(graph)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Initialize the distance matrix with the given graph's adjacency matrix
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Update the distance matrix with the shortest paths
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 3, float('inf'), 5],
        [2, 0, float('inf'), 4],
        [float('inf'), 1, 0, float('inf')],
        [float('inf'), float('inf'), 2, 0]
    ]

    shortest_paths = floyd_warshall(graph)
    for row in shortest_paths:
        print(row)