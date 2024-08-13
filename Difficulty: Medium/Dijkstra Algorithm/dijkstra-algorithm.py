import heapq

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist = [float('inf')] * V
        dist[S] = 0
        priority_queue = [(0, S)]
        
        while priority_queue:
            current_dist, u = heapq.heappop(priority_queue)
            
            if current_dist > dist[u]:
                continue
            
            for v, weight in adj[u]:
                if weight + dist[u] < dist[v]:
                    dist[v] = weight + dist[u]
                    heapq.heappush(priority_queue, (dist[v], v))
        
        return dist
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends