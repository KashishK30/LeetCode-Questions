class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0

        m = len(triangle)

        if m == 0:
            return 0
        if m == 1:
            return triangle[0][0]
        
        for row in range(m - 2, -1, -1 ):
            for column in range(len(triangle[row])):
                triangle[row][column] = triangle[row][column] + min(triangle[row + 1][column], triangle[row + 1][column + 1])
        return triangle[0][0]
        
            