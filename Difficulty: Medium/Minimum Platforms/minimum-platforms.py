#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        # platform = 0
        # max_platform = 0
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #       i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #       j
               
        #       dep[j] >= arr[i]:
        #           platform += 1  (1)
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #             i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #         j
        #             dep[j] <= arr[i]:
        #           platform -= 1 (0 )
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #               i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #             j
        #             dep[j] >= arr[i]:
        #           platform += 1 (1)
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #                   i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #             j
        #             dep[j] >= arr[i]:
        #           platform += 1 (2)
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #                         i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #             j
        #             dep[j] >= arr[i]:
        #           platform += 1 (3)
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #                             i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #               j
        #             dep[j] <= arr[i]:
        #           platform -= 1 (2)
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #                             i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #                     j
        #             dep[j] <= arr[i]:
        #           platform -= 1 (1)
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #                             i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #                         j
        #             dep[j] <= arr[i]:
        #           platform -= 1 (0)
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #                             i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #                                 j
        #             dep[j] >= arr[i]:
        #           platform += 1 (1)
        # arr = [900, 940, 950, 1100, 1500, 1800]
        #                                     i
        # dep = [910, 1120, 1130, 1200, 1900, 2000]
        #                                 j
        #             dep[j] >= arr[i]:
        #           platform += 1 (2)
        
        arr.sort()
        dep.sort()
        
        # Initialize pointers for arrivals and departures
        i = 0
        j = 0
        platform_needed = 0
        max_platforms = 0
        
        # Traverse both arrays
        while i < len(arr) and j < len(dep):
            # If next event is arrival, increment platform count
            if arr[i] <= dep[j]:
                platform_needed += 1
                i += 1
            # If next event is departure, decrement platform count
            else:
                platform_needed -= 1
                j += 1
            
            # Update the maximum platforms needed
            if platform_needed > max_platforms:
                max_platforms = platform_needed
        
        return max_platforms

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends