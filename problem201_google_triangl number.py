'''
This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. 
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. 
For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
'''


import unittest

class Solution:

    def findMaxWeight(self, triangle):
        max_val = triangle[0][0]
        for i in range(1, len(triangle)):
            N = len(triangle[i])
            for j in range(N):
                if j==0:
                    triangle[i][j] += triangle[i-1][j]
                elif j==N-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += max(triangle[i-1][j-1:j+1])

                if max_val < triangle[i][j]:
                    max_val = triangle[i][j]
        
        return max_val


class SolutionTestUnit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_triangle(self):
        triangle = [[1], [2, 3], [1, 5, 1]]
        self.assertEqual(self.solution.findMaxWeight(triangle), 9)


if __name__ == "__main__":
    unittest.main()