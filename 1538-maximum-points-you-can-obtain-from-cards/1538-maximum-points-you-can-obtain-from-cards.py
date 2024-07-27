class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        total_sum = sum(cardPoints)

        if k == len(cardPoints):
            return total_sum
        
        if k == 0:
            return 0

        window_size = n - k
        min_subarray_sum = float('inf')
        current_window_sum = 0

        for i in range(window_size):
            current_window_sum += cardPoints[i]
        min_subarray_sum = current_window_sum

        for i in range(window_size, n):
            current_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_subarray_sum = min(min_subarray_sum, current_window_sum)

        max_score = total_sum - min_subarray_sum

        return max_score
        

