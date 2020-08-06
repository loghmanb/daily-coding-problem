'''
Largest area of rectangle with permutations
Asked in: Directi

https://www.interviewbit.com/problems/largest-area-of-rectangle-with-permutations/

Problem Setter: amitkgupta94 Problem Tester: RAMBO_tejasv
Given a binary grid i.e. a 2D grid only consisting of 0’s and 1’s, 
find the area of the largest rectangle inside the grid such that 
all the cells inside the chosen rectangle should have 1 in them. 
You are allowed to permutate the columns matrix i.e. 
you can arrange each of the column in any order in the final grid. 
Please follow the below example for more clarity.

Lets say we are given a binary grid of 3 * 3 size.

1 0 1

0 1 0

1 0 0

At present we can see that max rectangle satisfying 
the criteria mentioned in the problem is of 1 * 1 = 1 area i.e 
either of the 4 cells which contain 1 in it. Now since 
we are allowed to permutate the columns of the given matrix, 
we can take column 1 and column 3 and make them neighbours. 
One of the possible configuration of the grid can be:

1 1 0

0 0 1

1 0 0

Now In this grid, first column is column 1, second column is column 3 
and third column is column 2 from the original given grid. 
Now, we can see that if we calculate the max area rectangle, 
we get max area as 1 * 2 = 2 which is bigger than the earlier case. 
Hence 2 will be the answer in this case.
'''
import unittest

from collections import Counter

# @param A : list of list of integers
# @return an integer
def solve(A):
    rows = len(A)
    if rows == 0:
        return 0
    cols = len(A[0])
    poles = [[0 for _ in range(cols)]]
    for r in range(rows):
        prev = poles[-1]
        poles.append([x if x == 0 else p + x for p, x in zip(prev, A[r])])
        
    res = 0
    for line in poles:
        sorted_line = sorted(Counter(line).items(), reverse=True)
        cum_width = 0
        for height, width in sorted_line:
            cum_width += width
            res = max(res, cum_width * height)

    return res


class LargestRectTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, solve([
              [1, 0, 1],
              [1, 1, 0],
              [1, 0, 0],
             ]))

    def test_2(self):
        self.assertEqual(2, solve([
              [1, 0, 1],
              [0, 1, 0],
              [1, 0, 0],
             ]))


if __name__ == "__main__":
    unittest.main()