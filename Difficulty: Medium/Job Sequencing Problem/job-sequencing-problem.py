#User function Template for python3
'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    # code here
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key = lambda x: x.profit, reverse = True)
        
        total_profit = 0
        job_count = 0
        
        max_deadline = max(Jobs, key = lambda x: x.deadline).deadline
        
        day_profit = [-1] * (max_deadline + 1)
        
        for job in Jobs:
            for j in range(job.deadline, 0, -1):
                if day_profit[j] == -1:
                    day_profit[j] = job.profit
                    total_profit += job.profit
                    job_count += 1
                    break
        return job_count, total_profit
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])

# } Driver Code Ends