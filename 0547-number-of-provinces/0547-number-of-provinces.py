class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city: int):
            for neighbor, connected in enumerate(isConnected[city]):
                if connected == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        n = len(isConnected)
        visited = [False] * n
        num_provinces = 0
        
        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                num_provinces += 1
        
        return num_provinces