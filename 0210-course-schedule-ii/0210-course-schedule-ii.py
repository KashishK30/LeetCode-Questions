class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for a, b in prerequisites:
            in_degree[a] += 1
            graph[b].append(a)
            
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbour in graph[course]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
                    
        if len(order) == numCourses:
            return order
        else:
            return []
            