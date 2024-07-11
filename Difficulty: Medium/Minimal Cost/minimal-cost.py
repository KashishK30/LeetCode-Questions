#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def minimizeCost(self, height, n, k):
        # code here
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(max(0, i - k), i):
                dp[i] = min(dp[i], dp[j] + abs(height[i] - height[j]))
        
        return dp[n - 1]

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        obj = Solution()
        print(obj.minimizeCost(arr, N, K))
# } Driver Code Ends