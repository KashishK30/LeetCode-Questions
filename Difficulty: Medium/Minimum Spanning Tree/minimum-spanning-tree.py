#User function Template for python3
import heapq

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        in_mst = [False] * V
        key = [float('inf')] * V
        
        key[0] = 0
        
        priority_queue = [(0, 0)] # key, vertex
        
        total_weight = 0
        
        while priority_queue:
            weight, u = heapq.heappop(priority_queue)
            
            if in_mst[u]:
                continue
            
            in_mst[u] = True
            
            total_weight += weight
            
            for neighbor in adj[u]:
                v, w = neighbor
                
                if not in_mst[v] and key[v] > w:
                    key[v] = w
                    
                    heapq.heappush(priority_queue, (w, v))
                    
        return total_weight


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends