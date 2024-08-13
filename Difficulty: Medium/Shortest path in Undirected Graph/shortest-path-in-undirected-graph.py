#User function Template for python3
from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)    
        
        dist = [-1] * (n)
        dist[src] = 0
        
        queue = deque([src])
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
                    
        return dist
                
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends