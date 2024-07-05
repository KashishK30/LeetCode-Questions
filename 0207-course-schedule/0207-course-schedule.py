class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            in_degree[dest] += 1
            graph[src].append(dest)
            
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        processed_courses = 0
        
        while queue:
            course = queue.popleft()
            processed_courses += 1
            for neighbour in graph[course]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
                    
        return processed_courses == numCourses