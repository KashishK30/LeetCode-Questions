class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        ## Bipartite BFS
        n = len(graph)
        color = [-1] * n

        def bfs(start):
            queue = deque([start])

            color[start] = 0

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = color[node] + 1
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True
        
        # TC: O(V + E)
        # SC: O(V)

        ## Bipartite DFS

        # color = [-1] * len(graph)

        # def dfs(node, c):
        #     color[node] = c

        #     for neighbor in graph[node]:
        #         if color[neighbor] == -1:
        #             if not dfs(neighbor, 1 - c):
        #                 return False
        #         elif color[neighbor] == color[node]:
        #             return False
        #     return True

        # for i in range(len(graph)):
        #     if color[i] == -1:
        #         if not dfs(i, 0):
        #             return False
        # return True

        # TC: O(N)
        # SC: O(1)
                