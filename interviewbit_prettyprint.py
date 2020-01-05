'''
PRETTYPRINT

https://www.interviewbit.com/problems/prettyprint/

Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
Example 2:

Input: A = 3.
Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.

'''
# @param A : integer
# @return a list of list of integers
def prettyPrint(A):
    B = [[0]*(2*A-1) for _ in range(2*A-1)]
    for i in range(2*A-1):
        if i<A:
            end = A-i
        else:
            end = i - A + 2
        for j in range(2*A-1):
            if j<A:
                k = A-j
            else:
                k = j-A+2
            if k<end:
                k = end
            B[i][j] = k
    return B


if __name__ == "__main__":
    data = [
        [3,
            [
                [3, 3, 3, 3, 3],
                [3, 2, 2, 2, 3],
                [3, 2, 1, 2, 3],
                [3, 2, 2, 2, 3],
                [3, 3, 3, 3, 3],
            ]
        ]
    ]

    for d in data:
        print('input', d[0], 'output', prettyPrint(d[0]))