#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        
        # Initialize a visited list to keep track of visited vertices
        visited = [False] * V
        
        # List to store the DFS traversal result
        traversal = []
        
        def dfs(node):
            
            # Mark the current node as visited
            visited[node] = True
            
            # Add the node to the traversal list
            traversal.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
                    
        dfs(0)
            
        return traversal
#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends