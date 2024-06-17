class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
        if c == 0:
            return True
        for a in range(int(math.sqrt(c)) + 1):
            b_squared = c - a * a
            b = int(math.sqrt(b_squared))
            if b*b == b_squared:
                return True
            
        return False