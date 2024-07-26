class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * col
        max_area = 0

        for row in matrix:
            for i in range(col):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            max_area = max(max_area, self.largestRectangle(heights))
        
        return max_area

    def largestRectangle(self, heights):
        stack = []
        max_area = 0
        index = 0

        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
            ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

        return max_area