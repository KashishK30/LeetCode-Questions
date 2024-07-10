class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        a = 1
        b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b