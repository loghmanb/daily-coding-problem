'''
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

Solution from https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
'''

moves = set([(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)])
 
def is_valid_move(board, i, j, mov):
    N = len(board)
    i += mov[0]
    j += mov[1]
    return bool(i>=0 and i<N and j>=0 and j<N and board[i][j]==-1)


def run_knight_tours(board, i, j, pos):
    N = len(board)
    if (pos==N*N):
        return True
    for mov in moves:
        if is_valid_move(board, i, j, mov):
            board[i+mov[0]][j+mov[1]] = pos
            if run_knight_tours(board, i+mov[0], j+mov[1], pos+1):
                return True
            board[i+mov[0]][j+mov[1]] = -1
    return False


def knight_tours(N):
    if N<2: return 0
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[0][0] = 0
    run_knight_tours(board, 0, 0, 1)
    return board

def print_board(board):
    for i in range(board):
        print(board[i])

if __name__ == "__main__":
    data = [
            [8, ]
    ]
    for d in data:
        print('input', d[0], 'output')
        board = knight_tours(d[0])
        print_board(board)
