'''
Min Sum Path in Matrix
Asked in: Amazon

https://www.interviewbit.com/problems/min-sum-path-in-matrix/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

 Note: You can only move either down or right at any point in time. 
Example :

Input : 

    [  1 3 2
       4 3 1
       5 6 1
    ]

Output : 8
     1 -> 3 -> 2 -> 1 -> 1
'''

# @param mat : list of list of integers
# @return an integer
def minPathSum(mat):
    n = len(mat)
    m = len(mat[0])
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = mat[i][j]
            if i==0:
                if j>0:
                    ans[i][j] += ans[i][j-1]
            elif j==0:
                ans[i][j] += ans[i-1][j]
            else:
                ans[i][j] += min(ans[i-1][j], ans[i][j-1])
    return ans[-1][-1]


if __name__ == "__main__":
    data = [
            [
             [[1, 3, 2],
              [4, 3, 1],
              [5, 6, 1]],
              8
            ]
    ]
    for d in data:
        print('input', d[0], 'output', minPathSum(d[0]))