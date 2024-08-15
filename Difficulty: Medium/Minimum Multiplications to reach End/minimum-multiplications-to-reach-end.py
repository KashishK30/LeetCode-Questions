#User function Template for python3
from collections import deque
from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        MOD = 100000
        
        queue = deque([(start, 0)])
        
        visited = set([start])
        
        while queue:
            current, steps = queue.popleft()
            
            if current == end:
                return steps
            
            for num in arr:
                new_value = (current * num) % MOD
                
                if new_value not in visited:
                    visited.add(new_value)
                    queue.append((new_value, steps + 1))
                
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends