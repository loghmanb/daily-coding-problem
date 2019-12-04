'''
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
'''

LEFT2RIGHT = 1
UP2DOWN = 2
RIGHT2LEFT = 3
DOWN2UP = 4

def print_clock_wise(A):
    ans = []

    N = len(A)
    M = len(A[0])

    start_row, end_row = 0, N-1
    start_col, end_col = 0, M-1

    direction = LEFT2RIGHT
    i, j = 0, 0
    for _ in range(N*M):
        ans.append(A[i][j])
        if direction == LEFT2RIGHT:
            if j<end_col: 
                j += 1
            else:
                direction = UP2DOWN
                start_row += 1
                i += 1
        elif direction == UP2DOWN:
            if i<end_row:
                i += 1
            else:
                direction = RIGHT2LEFT
                end_col -= 1
                j -= 1
        elif direction == RIGHT2LEFT:
            if j>start_col:
                j -= 1
            else:
                direction = DOWN2UP
                end_row -= 1
                i -= 1
        elif direction == DOWN2UP:
            if i>start_row:
                i -= 1
            else:
                direction = LEFT2RIGHT
                start_col += 1
                j += 1

    return ans


if __name__ == "__main__":
    data = [
            [
             [
              [1,  2,  3,  4,  5],
              [6,  7,  8,  9,  10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20]
             ], [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
            ]
    ]

    for d in data:
        print('input', d[0], print_clock_wise(d[0]))
