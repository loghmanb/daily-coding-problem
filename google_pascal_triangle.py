'''
https://www.interviewbit.com/problems/pascal-triangle/

Pascal Triangle

Asked in: Google, Amazon

Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
'''

# @param n : integer
# @return a list of list of integers
def solve(n):
    A = [[1] for _ in range(n)]
    for i in range(1, n):
        for j in range(i, n):
            val = 0
            m = len(A[j-1])
            if i<=m-1:
                val = A[j-1][i]
            if i<=m:
                val += A[j-1][i-1]
            if val==0:
                val = 1
            A[j].append(val)
    return A


if __name__=='__main__':
    data = [
            [5,
                [
                    [1],
                    [1,1],
                    [1,2,1],
                    [1,3,3,1],
                    [1,4,6,4,1]
                ]
            ]
    ]

    for d in data:
        print('input', d[0], 'output', solve(d[0]))

