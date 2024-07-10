class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return safe[node]
            
            visiting.add(node)
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            visiting.remove(node)
            visited.add(node)
            safe[node] = True
            return True

        for i in range(n):
            if i not in visited:
                dfs(i)
        
        return [i for i in range(n) if safe[i]]