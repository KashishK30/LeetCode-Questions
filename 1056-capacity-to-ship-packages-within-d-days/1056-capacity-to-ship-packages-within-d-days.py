class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def func(capacity):
            current_weight = 0
            required_days = 1
            for weight in weights:
                if current_weight + weight > capacity:
                    required_days += 1
                    current_weight = 0
                current_weight += weight
                if required_days > days:
                    return False
            return True                
                 
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2
            if func(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left