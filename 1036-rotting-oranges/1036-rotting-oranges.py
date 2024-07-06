class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh_oranges = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if fresh_oranges == 0:
            return 0

        minutes = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue and fresh_oranges > 0:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_oranges -= 1
        
        return minutes if fresh_oranges == 0 else -1