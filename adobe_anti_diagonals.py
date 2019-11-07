'''
Anti Diagonals

https://www.interviewbit.com/problems/anti-diagonals/

Asked in: Microsoft, Adobe

Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]

'''

# @param A : list of list of integers
# @return a list of list of integers
def diagonal(A):
    N = len(A)
    ans = []
    for i in range(N):
        for j in range(N):
            k = i + j
            if k==len(ans):
                ans.append([])
            ans[k].append(A[i][j])
    return ans



if __name__=='__main__':
    data = [
        [
         [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
         ],
         [
            [1],
            [2, 4],
            [3, 5, 7],
            [6, 8],
            [9]
         ]
        ]
    ]
    for d in data:
        print('input', d[0], 'output', diagonal(d[0]))