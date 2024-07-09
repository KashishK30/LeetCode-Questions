class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return

        row = len(grid)
        col = len(grid[0])

        def bfs(x, y):
            queue = deque([(x, y)])
            grid[x][y] = -1

            while queue:
                r, c = queue.popleft()
                
                for dr, dc in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                    new_r = dr + r
                    new_c = dc + c
                    if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = -1
                        queue.append((new_r, new_c))

        count = 0

        for i in range(row):
            if grid[i][0] == 1:
                bfs(i, 0)
            if grid[i][col - 1] == 1:
                bfs(i, col - 1)

        for j in range(col):
            if grid[0][j] == 1:
                bfs(0, j)
            if grid[row - 1][j] == 1:
                bfs(row - 1, j)
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += 1

        return count
        
