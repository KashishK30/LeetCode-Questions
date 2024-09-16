class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        my_dict = {i: 0 for i in range(1, n**2 + 1)}
        result = []

        for i in range(n):
            for j in range(n):
                my_dict[grid[i][j]] += 1

        missing = -1
        repeated = -1

        for key in my_dict:
            if my_dict[key] == 0:
                missing = key
            elif my_dict[key] == 2:
                repeated = key
        
        result.append(repeated)
        result.append(missing)

        return result
    # TC: O(n ^ 2) + O(n ^ 2) + O(n ^ 2) = 
    # Initialization of the Dictionary + Counting Occurrences in the Grid + Finding Missing and Repeated Values
    # SC: O(n ^ 2) Dictionary stores 1 to n ^ 2 elements + O(1) the result stores 2 elements

