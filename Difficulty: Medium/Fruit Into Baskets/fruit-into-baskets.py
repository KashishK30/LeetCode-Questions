#User function Template for python3

class Solution:
    def totalFruits(self,arr):
        # Code here

        fruit_count = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(arr)):
            if arr[right] in fruit_count:
                fruit_count[arr[right]] += 1
            else:
                fruit_count[arr[right]] = 1
                
            while len(fruit_count) > 2:
                fruit_count[arr[left]] -= 1
                if fruit_count[arr[left]] == 0:
                    del fruit_count[arr[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        # N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalFruits(arr)
        print(res)

# } Driver Code Ends