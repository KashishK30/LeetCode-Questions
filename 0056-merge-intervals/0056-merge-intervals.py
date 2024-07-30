class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key = lambda x: x[0])

        result = [intervals[0]]

        for current in intervals[1:]:
            last_merged = result[-1]

            if current[0] <= last_merged[1]:
                last_merged[1] = max(current[1], last_merged[1])
            else:
                result.append(current)
        return result