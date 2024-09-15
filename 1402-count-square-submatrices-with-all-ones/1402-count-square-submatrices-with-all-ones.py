class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Space Optimization
        m = len(matrix)
        n = len(matrix[0])

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        sum_squares = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    curr[j] = min(curr[j - 1], prev[j - 1], prev[j]) + 1
                    sum_squares += curr[j]
                else:
                    curr[j] = 0
            prev, curr = curr, [0] * (n + 1)
        return sum_squares

        # TC: O(m * n)
        # SC: O(n)

        # # Tabulation
        # m = len(matrix)
        # n = len(matrix[0])

        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # sum_squares = 0

        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if matrix[i - 1][j - 1] == 1:
        #             dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        #             sum_squares += dp[i][j]

        # return sum_squares
        # # TC: O(m * n)
        # # SC: O(m * n)