def dijkstra(graph, start):
    # Initialize distances to infinity for all vertices except the start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        # Find the vertex with the minimum distance
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # If the minimum distance is infinity, we have reached the end
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_vertex):
            distance = (
                distances[current_vertex]
                + graph[current_vertex][neighbor]["weight"]
            )

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Remove the current vertex from the unvisited set
        unvisited.remove(current_vertex)

    return distances
