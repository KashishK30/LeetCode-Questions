from typing import List
from collections import deque, defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)

            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            queue = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            sorted_order = []

            while queue:
                node = queue.popleft()
                sorted_order.append(node)
                for neighbour in graph[node]:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)

            return sorted_order if len(sorted_order) == k else []

        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)

        if not row_order or not col_order:
            return []

        row_index = {num: i for i, num in enumerate(row_order)}
        col_index = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]

        for num in row_order:
            row_pos = row_index[num]
            col_pos = col_index[num]
            matrix[row_pos][col_pos] = num
        
        return matrix
