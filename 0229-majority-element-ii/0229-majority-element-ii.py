from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
    # BOYER-MOORE VOTING ALGORITHM

        # Step 1: Find the potential candidates
        if not nums:
            return []
        
        n = len(nums)

        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step2: Verify the candidates
        count1, count2 = 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
        
        result = []
        if count1 > (n//3):
            result.append(candidate1)
        if count2 > (n//3):
            result.append(candidate2)
        
        return result

    # TC: O(n): for both finding and verifying elements
    # SC: O(1): uses fixed extra space regardless of the input size

    
    # # Solution 1
    #     n = len(nums)
    #     count_num = Counter(nums)
    #     result = []

    #     for num, count in count_num.items():
    #         if count > n//3:
    #             result.append(num)
    #     return result
    # # TC: O(n)
    # # SC: O(k)
    