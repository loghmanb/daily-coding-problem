# Coding test interview from Solar Monkey
#
# You are about to write the implementation of the `solution_valid(board)`
# # function. It should return True when the solution is True, False otherwise.
# # The cells of the sudoku board may also contain 0's, which represent empty
# # cells. Boards with empty cells are invalid of course. For the standard rules
# # see https://en.wikipedia.org/wiki/Sudoku
#
# # However, before you begin, think about the parts of this problem, and chop it
# # up. Write tests in TDD fashion for subproblems and their functions.


from collections import defaultdict

def solution_valid(board):   
    #check row and column is distict no or not?!
    rows = defaultdict(int)
    columns = defaultdict(int)
    squares = defaultdict(int)
    for i in range(9):
        for j in range(9):
            columns[board[i][j]] += 1
            rows[board[j][i]] += 1
            new_j = (i*3 + j%3)%9
            new_i = (i//3)*3 + j//3
            squares[board[new_i][new_j]] += 1

    for i in range(1, 10):
        if columns[i]!=9 or columns[i]!=9 or squares[i]!=9:
           return False
            
    return True
   

if __name__ == "__main__":
    def print_mat(mat):
        for l in mat:
            print(l)

    data = [
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [9, 1, 2, 3, 4, 5, 6, 7, 8],
            ],
            [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ]
        ]

    for d in data:
        print('check validation for', print_mat(d), 'is', solution_valid(d))