class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        trust_count = [0] * (n + 1)
        trust_others = [0] * (n + 1)
        
        for a, b in trust:
            trust_count[b] += 1
            trust_others[a] += 1
        
        for i in range(1, n + 1):
            if trust_count[i] == n - 1 and trust_others[i] == 0:
                return i
        
        return -1
        