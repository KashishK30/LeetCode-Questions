class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for char in logs:
            if char == "../":
                if count > 0:
                    count -= 1
            elif char == "./":
                continue
            else:
                count += 1

        return count