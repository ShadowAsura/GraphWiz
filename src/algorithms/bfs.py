from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    path = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return path
