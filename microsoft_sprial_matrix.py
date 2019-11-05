'''
Spiral Order Matrix II

Asked in: Microsoft, JP Morgan, Amazon

https://www.interviewbit.com/problems/spiral-order-matrix-ii/

Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Input Format:

The first and the only argument contains an integer, A.
Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:

1 <= A <= 1000
Examples:

Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    4

Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]

'''

# @param A : integer
# @return a list of list of integers
def generateMatrix(n):
    mat = [[0]*n for _ in range(n)]
        
    row_start, col_start = 0, 0
    row_end, col_end = n-1, n-1
    i, j = 0, 0
    i_dir, j_dir = 0, 1
    for k in range(1, n*n+1):
        mat[i][j] = k
        j += j_dir
        if j>col_end:
            j = col_end
            row_start += 1
            j_dir = 0
            i_dir = 1
        elif j<col_start:
            j = col_start
            row_end -= 1
            j_dir = 0
            i_dir = -1
            i += i_dir
        i += i_dir
        if i>row_end:
            i = row_end
            col_end -= 1
            j_dir = -1
            i_dir = 0
            j -= 1
        elif i<row_start:
            i = row_start
            col_start += 1
            j_dir = 1
            i_dir = 0
            j += 1
            
    return mat


if __name__ == "__main__":
    data = [
            [3, 
                [ 1, 2, 3 ],
                [ 8, 9, 4 ],
                [ 7, 6, 5 ]
            ]
    ]

    for d in data:
        print('input', d[0], 'output', generateMatrix(d[0]))