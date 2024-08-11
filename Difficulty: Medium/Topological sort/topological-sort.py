from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here

        # Kahn's Algorithm (BFS-based approach)
        
        # 1. Compute in-degree
        # 2. Queue with indegree 0
        # 3. while queue is non empty
        # deque a vertex u and add it to topo order
        # For each adj vertex v of u reduce it's indegree by 1
        # If v's indegree becomes 0, enqueue v
        # 4. If the topo order contains all vertices : True
        in_degree = [0] * V
        
        for i in range(V):
            for j in adj[i]:
                in_degree[j] += 1
        
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topo_order) == V:
            return topo_order
        else:
            return []
                
        

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends