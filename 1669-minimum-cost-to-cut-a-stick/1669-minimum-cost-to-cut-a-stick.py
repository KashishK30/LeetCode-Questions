class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # # Tabulation

        # # Add the two elements(0 and n) to the cuts array and sort it
        # cuts = [0] + cuts + [n]
        # cuts.sort()

        # c = len(cuts)

        # # Create a dp array initialized to 0
        # dp = [[0 for _ in range(c)] for _ in range(c)]

        # # Iterate over the length of each segment
        # for length in range(2, c): # length starts with 2 (subproblem with atleast one cut)
        #     for i in range(c - length): # i is the starting point
        #         j = i + length # j is the ending point
        #         dp[i][j] = float('inf') # Initialize the cost as infinity

        #         # Try all possible cuts between i and j and choose the one with minimum cost
        #         for k in range(i + 1, j):
        #             cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
        #             dp[i][j] = min(cost, dp[i][j])

        # # The answer will be in dp[0][c - 1], i.e. , the start and the end of the string
        # return dp[0][c - 1]

        # TC: O(n * n * n)
        # SC: O(n * n)

        # Memoization

        cuts = [0] + sorted(cuts) + [n]
        c = len(cuts)

        dp = [[ -1 for _ in range(c)] for _ in range(c)]

        def memoization(i, j):
            if i + 1 == j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            min_cost = float('inf')

            for k in range(i + 1, j):
                cost = (cuts[j] - cuts[i]) + memoization(i, k) + memoization(k, j)
                min_cost = min(cost, min_cost)

            dp[i][j] = min_cost

            return min_cost
        return memoization(0, c - 1)