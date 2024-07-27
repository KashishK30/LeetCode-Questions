class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):
            char_count[s[right]] += 1

            while all(char_count[char] > 0 for char in 'abc'):
                count += len(s) - right
                char_count[s[left]] -= 1
                left += 1
        return count