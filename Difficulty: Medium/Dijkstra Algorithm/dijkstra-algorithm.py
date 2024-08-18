import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist = [float('inf')] * V
        dist[S] = 0
        
        pq = [(0, S)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > dist[u]:
                continue
            
            for neighbor, weight in adj[u]:
                distance = weight + current_dist
                
                if dist[neighbor] > distance:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
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