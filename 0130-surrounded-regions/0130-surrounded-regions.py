class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        row = len(board)
        col = len(board[0])

        def bfs(x, y):
            queue = deque([(x, y)])
            board[x][y] = "T"

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if 0 <= new_r < row and 0 <= new_c < col  and board[new_r][new_c] == "O":
                            board[new_r][new_c] = "T"
                            queue.append((new_r, new_c))
        for i in range(row):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)
        
        for j in range(col):
            if board[0][j] == "O":
                bfs(0, j)
            if board[row - 1][j] == "O":
                bfs(row - 1, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(row):
            for j in range(col):
                if board[i][j] == "T":
                    board[i][j] = "O"
        return board

        

        