class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Bipartite DFS

        color = [-1] * len(graph)

        def dfs(node, c):
            color[node] = c

            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
                