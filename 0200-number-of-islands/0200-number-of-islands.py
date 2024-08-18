class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if not grid:
            return 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0':
                return 

            grid[r][c] = '0'

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        num_islands = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    num_islands += 1

                    dfs(row, col)

        return num_islands