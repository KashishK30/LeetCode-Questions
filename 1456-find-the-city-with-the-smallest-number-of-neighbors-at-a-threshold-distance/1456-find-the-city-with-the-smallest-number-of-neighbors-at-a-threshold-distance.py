class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            distance[i][i] = 0
        
        for u, v, w in edges:
            distance[u][v] = w
            distance[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
        
        min_reachable = n
        best_city = -1

        for i in range(n):
            reachable_count = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    reachable_count += 1
        
            if reachable_count <= min_reachable:
                min_reachable = reachable_count
                best_city = i
        
        return best_city