'''
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, 
exists(board, "SEE") returns true, 
exists(board, "ABCB") returns false.
'''

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Board:
    def __init__(self, board):
        self.board = board
        self.N = len(board)
        self.M = len(board[0])


    def _check_exists(self, string, item):
        if not string: return True
        
        is_found = False
        row, col = item
        if 0<=row<self.N and 0<=col<self.M \
                and self.board[row][col]==string[0]:
            self.board[row][col] = (string[0],)
            for mov in DIRECTION:
                if self._check_exists(string[1:], (row+mov[0], col+mov[1])):
                    is_found = True
                    break
            self.board[row][col] = string[0]
        return is_found


    def exists(self, string):
        start_points = []
        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j]==string[0]:
                    start_points.append((i,j))

        for item in start_points:
            if self._check_exists(string, item):
                return True
        return False


if __name__ == "__main__":
    data = [
            ["ABCCED", True],
            ["SEE", True],
            ["ABCB", False]
    ]
    board = Board(
                    [
                    ['A','B','C','E'],
                    ['S','F','C','S'],
                    ['A','D','E','E']
                  ])
    for d in data:
        print('input', d[0], 'output', board.exists(d[0]))