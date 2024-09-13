class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Compute the XOR array
        # Initialize an array to store the XOR values
        n = len(arr)
        prefix = [0] * n

        # The first prefix value is the first element itself
        prefix[0] = arr[0]

        # Compute prefix XOR of all element from arr[1] to arr[n - 1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]

        # Answer each query, using the precomputed prefix value
        result = []
        for left, right in queries:
            # If left is 0, we can directly use the prefix value
            if left == 0:
                result.append(prefix[right])
            else:
                # XOR from left to right is derived as:
                # prefix[right] ^ prefix[left - 1]
                # This excludes the elements before 'left'
                result.append(prefix[right] ^ prefix[left - 1])
        return result
        
# # Input Handling

# # Step 1: Take input for the array
# arr = list(map(int, input().split()))

# # Step 2: Take input for the number of queries
# q = int(input())

# # Step 3: Take input for each query and store in the queries list
# queries = []
# for _ in range(q):
#     left, right = map(int, input().split())
#     queries.append([left, right])

# # Step 4: Compute results using xorQueries function
# output = xorQueries(arr, queries)

# # Step 5: Output the result for each query
# print()
# for result in output:
#     print(result)