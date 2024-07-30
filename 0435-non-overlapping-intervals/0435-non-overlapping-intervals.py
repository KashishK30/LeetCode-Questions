class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        count = 0

        intervals.sort(key = lambda x: x[1])

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end <= intervals[i][0]:
                prev_end = intervals[i][1]
            else:
                count += 1
        
        return count
