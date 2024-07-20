class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)

        dp = [[0] * n for _ in range(m)]

        i = 0
        j = 0
        while i < m and j < n:
            dp[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= dp[i][j]
            colSum[j] -= dp[i][j]

            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        return dp