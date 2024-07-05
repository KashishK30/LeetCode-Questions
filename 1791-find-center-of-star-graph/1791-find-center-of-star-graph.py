class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        
        if n == 1:
            return 1
        
        degree = [0] * (n + 1)
         
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            
        max_degree = max(degree[1:])
        
        for i in range(1, n + 1):
            if degree[i] == max_degree:
                return i
        
        return -1