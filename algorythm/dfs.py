def dfs(graph, start_vertex):
    visited = set()
    # Use a stack to keep track of vertices to visit
    stack = [start_vertex]
    while stack:
        # Take the last vertex from the stack
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            # Mark the vertex as visited
            visited.add(vertex)
            # Add the neighbors of the vertex to the stack
            stack.extend(graph[vertex])

    return visited
