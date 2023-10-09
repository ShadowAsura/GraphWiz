def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            stack.extend(n for n in graph[node] if n not in visited)

    return traversal_order


