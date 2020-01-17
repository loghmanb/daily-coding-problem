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

import unittest

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


class TestDiagonalFunction(unittest.TestCase):
    
    def test_diagonal_empty_array(self):
        result = diagonal([])
        expected = []
        self.assertEqual(expected, result)

    def test_diagonal_with_data(self):
        result = diagonal([
                            [1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                          ])
        expected = [
                    [1],
                    [2, 4],
                    [3, 5, 7],
                    [6, 8],
                    [9]
                   ]
        self.assertEqual(expected, result, 'Error whith 3 dimension array')


if __name__=='__main__':
    
    unittest.main()