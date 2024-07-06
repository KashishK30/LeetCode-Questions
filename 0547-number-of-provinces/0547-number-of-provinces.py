class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]
        
        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootY] > rank[rootX]:
                parent[rootX] = rootY
            else:
                parent[rootX] =rootY
                rank[rootY] += 1

        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(parent, rank, i, j)

        province_count = len(set(find(parent, i) for i in range(n)))
        return province_count