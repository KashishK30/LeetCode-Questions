class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        # Build graph adjacency list for directional edges
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # Assuming bi-directional connections, if applicable
        
        # BFS setup
        queue = deque([source])
        visited = [False] * n
        visited[source] = True
        
        # BFS traversal
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if neighbour == destination:
                        return True
                    visited[neighbour] = True
                    queue.append(neighbour)
        
        # If destination not reached
        return False
            