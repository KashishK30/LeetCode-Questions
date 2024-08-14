class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        pq = [(0, 0, 0)]
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            current_effort, x, y = heapq.heappop(pq)

            if (x, y) == (rows - 1, cols - 1):
                return current_effort

            for dr, dc in directions:
                new_r = x + dr
                new_c = y + dc
                if (0 <= new_r < rows) and (0 <= new_c < cols):
                    next_effort = max(current_effort, abs(heights[x][y] - heights[new_r][new_c]))

                    if next_effort < efforts[new_r][new_c]:
                        efforts[new_r][new_c] = next_effort
                        heapq.heappush(pq, (next_effort, new_r, new_c))

        return -1