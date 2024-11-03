from collections import deque


def bfs(graph, start):
    # Empty set to store visited vertices
    visited = set()
    # Create a queue and enqueue the start vertex
    queue = deque([start])

    while queue:  # While queue is not empty keep looping
        # Take the first vertex from the queue
        vertex = queue.popleft()
        # Check if the vertex has not been visited
        if vertex not in visited:
            # If the vertex has not been visited, print it
            print(vertex, end=" ")
            # Mark the vertex as visited
            visited.add(vertex)
            # Add the neighbors of the vertex to the queue
            # Set difference is used to avoid adding the vertex again
            queue.extend(set(graph[vertex]) - visited)
    # Return the set of visited vertices
    return visited
