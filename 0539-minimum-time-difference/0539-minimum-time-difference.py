class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        result = []
        n = len(timePoints)
        min_diff = float('inf')

        for time_str in timePoints:
            hours, minutes = map(int, time_str.split(':'))
            result.append(hours * 60 + minutes)
            
        result.sort()

        for i in range(1, n):
            diff = abs(result[i] - result[i - 1])
            min_diff = min(diff, min_diff)

        circular_diff = (1440 - result[-1] + result[0])
        min_diff = min(min_diff, circular_diff)

        return min_diff

        # TC: O(n log(n))
        # SC: O(1)