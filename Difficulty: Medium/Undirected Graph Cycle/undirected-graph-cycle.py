from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        self.adj = adj
        self.visited = [False] * V
        self.parent = [-1] * V
        
        for v in range(V):
            if not self.visited[v]:
                if self.bfs(v):
                    return True
        return False
        
    def bfs(self, start):
        queue = deque([start])
        self.visited[start] = True
        
        while queue:
            v = queue.popleft()
            
            for neighbour in self.adj[v]:
                if not self.visited[neighbour]:
                    self.visited[neighbour] = True
                    self.parent[neighbour] = v
                    queue.append(neighbour)
                elif neighbour != self.parent[v]:
                    return True
        return False
                    

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends