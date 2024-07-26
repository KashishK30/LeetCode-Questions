#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        def knows(a, b):
            return M[a][b] == 1
            
        stack = list(range(n))
        
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if knows(a, b):
                stack.append(b)
            else:
                stack.append(a)
        
        if not stack:
            return -1
            
        candidate = stack.pop()
        
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1
        
        return candidate

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends