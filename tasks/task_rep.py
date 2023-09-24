"""
    В системе контроля версий SEHR GUT можно наследовать репозиторий и вносить изменения кода в какую либо версию кода.
При этом изменение, внесенное в версию кода, автоматически вносится во все репозитории, из которых был наследован код.

    Исходно в системе есть только репозиторий 0. Если от него были пронаследованы репозитории 1 и 2, а от репозитория 1
был наследован репозиторий 3 и изменения были внесены в репозиторий 3, то они также внесутся в репозитории 1 и 0
(но не в репозиторий 2).

    Вася хочет внести изменение в один репозиторий таким образом, чтобы они оказались в как можно большем количестве
репозиториев.
"""

n = int(input())
graph = {}
for i in range(n):
    node = int(input())
    if node not in graph:
        graph[node] = [i + 1]
        graph[i + 1] = []
    else:
        graph[node].append(i + 1)
        graph[i + 1] = []


def dfs_depth(graph, start):
    visited = set()
    stack = [(start, 0)]
    max_depth = (start, 0)

    while stack:
        node, depth = stack.pop()
        if depth > max_depth[1]:
            max_depth = (node, depth)

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, depth + 1))

    return max_depth


# Запуск DFS с начальной вершиной 'A'
max_node, max_depth = dfs_depth(graph, 0)

print(max_node)
