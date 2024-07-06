class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]

        if start_color == color:
            return image
        
        def dfs(r, c):
            if image[r][c] == start_color:
                image[r][c] = color

                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < len(image):
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < len(image[0]):
                    dfs(r, c + 1)
        dfs(sr, sc)
        return image