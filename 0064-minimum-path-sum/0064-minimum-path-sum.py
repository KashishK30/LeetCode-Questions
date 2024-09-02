class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        # Space Optimization
        m = len(grid)
        n = len(grid[0])

        # Initialize the prev row to store the minimum path sum of the fisrt row
        prev = [0] * n
        prev[0] = grid[0][0]

        # Fill the first row
        for j in range(1, n):
            prev[j] = grid[0][j] + prev[j - 1]
        
        # Compute the minimum path sum for each row
        for i in range(1, m):
            curr = [0] * n
            curr[0] = prev[0] + grid[i][0]
            for j in range(1, n):
                curr[j] = grid[i][j] + min(prev[j], curr[j - 1])
            prev = curr
            
        return prev[n - 1]

        # TC: O(m * n)
        # SC: O(n)

        # # Tabulation
        # m = len(grid)
        # n = len(grid[0])

        # dp = [[0 for _ in range(n)] for _ in range(m)]

        # # Initialize the Base Case
        # dp[0][0] = grid[0][0]

        # # Fill the 1st row
        # for j in range(1, n):
        #     dp[0][j] = (grid[0][j] + dp[0][j - 1])

        # # Fill the 1st column
        # for i in range(1, m):
        #     dp[i][0] = (grid[i][0] + dp[i - 1][0]) 

        # # Fill the rest of the table
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        
        # return dp[m - 1][n - 1]

        # # TC: O(m * n)
        # # SC: O(m * n)

        # # Memoization
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1 for _ in range(n)] for _ in range(m)]

        # def min_cost_path(grid, i, j, dp):
        #     # Base cases
        #     if i == 0 and j == 0:
        #         return grid[0][0]

        #     if i < 0 or j < 0:
        #         return float('inf') # Return large value for out of bound to signify invalid paths

        #     # if dp is already sorted
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     # Calculate the min cost to reach the current cell
        #     up = grid[i][j] + min_cost_path(grid, i - 1, j, dp) # Cost coming from above
        #     left = grid[i][j] + min_cost_path(grid, i, j - 1, dp) # Cost coming from left

        #     dp[i][j] = min(up, left)
        #     return dp[i][j]

        # return min_cost_path(grid, m - 1, n - 1, dp)

        # # TC: O(m * n)
        # # SC: O(m * n)