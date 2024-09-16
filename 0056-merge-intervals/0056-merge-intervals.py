class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        
        # Sort the elements based on the starting time
        intervals.sort()

        ans = []

        # Initialized with 1st interval
        for interval in intervals:
            # If ans is empty or current element does not overlap, add it to ans
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                # If ther is an overlap, merge the intervals by updating the end
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans

    # TC: O(n * log n)
    # Sorting: O(n * log n) uses tim sort
    # Merging: O(n)

    # SC: O(n)
    # Auxiliary Space for Sorting: O(1) sorting in place
    # Additional space for result: O(n)

