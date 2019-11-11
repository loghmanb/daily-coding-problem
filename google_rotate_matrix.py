'''
Rotate Matrix
Asked in:  
Google
Facebook
Amazon
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
'''

# @param A : list of list of integers
# @return the same list modified
def rotate(A):
    N = len(A)
    ans = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans[j][N-1-i] = A[i][j]
    return ans

if __name__ == "__main__":
    data = [
            [
                [
                 [1, 2],
                 [3, 4]
                ],
                [
                 [3, 1],
                 [4, 2]
                ]
            ]
           ] 
    
    for d in data:
        print('input', d[0], 'output', rotate(d[0]))
