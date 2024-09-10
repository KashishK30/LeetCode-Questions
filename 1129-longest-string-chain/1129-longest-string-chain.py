class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)

        words.sort(key=len)

        def is_predecessor(word1, word2):
            if len(word1) != len(word2) + 1:
                return False

            first = 0
            second = 0

            while first < len(word1):
                if second < len(word2) and word1[first] == word2[second]:
                    first += 1
                    second += 1
                else:
                    first += 1
            return first == len(word1) and second == len(word2)

        dp = [1] * n

        max_length = 1

        for ind in range(n):
            for prev_ind in range(ind):
                if is_predecessor(words[ind], words[prev_ind]) and 1 + dp[prev_ind] > dp[ind]:
                    dp[ind] = 1 + dp[prev_ind]
            if dp[ind] > max_length:
                max_length = dp[ind]
        return max_length