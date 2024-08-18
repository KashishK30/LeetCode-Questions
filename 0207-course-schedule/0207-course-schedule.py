class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # Khan's Algorithm (BFS algorithm)
        
        # graph = defaultdict(list)

        # in_degree = [0] * numCourses

        # for dest, src in prerequisites:
        #     graph[src].append(dest)
        #     in_degree[dest] += 1

        # queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # processed_courses = 0

        # while queue:
            
        #     processed_courses += 1

        #     node = queue.popleft()

        #     for neighbor in graph[node]:
        #         in_degree[neighbor] -= 1
        #         if in_degree[neighbor] == 0:
        #             queue.append(neighbor)
                    
        # return processed_courses == numCourses

        # DFS algorithm

        adj_list = [[] for _ in range(numCourses)]
        
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            
        visited = [0] * numCourses

        def dfs(courses):
            
            if visited[courses] == 1:
                return False

            if visited[courses] == 2:
                return True

            visited[courses] += 1

            for neighbor in adj_list[courses]:
                if not dfs(neighbor):
                    return False

            visited[courses] = 2
            return True

        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return False
        return True

