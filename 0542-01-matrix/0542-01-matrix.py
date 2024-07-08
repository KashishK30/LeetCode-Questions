class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat

        rows = len(mat)
        col = len(mat[0])
        dist = [[float('inf')] * col for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(col):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))


        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < rows and 0 <= new_c < col:
                    if dist[new_r][new_c] > dist[r][c] + 1:
                        dist[new_r][new_c] = dist[r][c] + 1
                        queue.append((new_r, new_c))
        return dist
