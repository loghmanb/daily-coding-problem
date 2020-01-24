'''
Diffk II
Asked in: Facebook

https://www.interviewbit.com/problems/diffk-ii/

Given an array A of integers and another non negative integer k, 
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2

Output :

1
as 3 - 1 = 2

Return 0 / 1 for this problem.
'''

import unittest
from collections import defaultdict

class Solution:

    def is_exists(self, nums, x1, x2):
        if x1==x2 and len(nums[x1])>1 or \
                x1 in nums and x2 in nums:
            return True
        return False

    # @param A : tuple of integers
    # @param K : integer
    # @return an integer
    def diffPossible(self, A, K):
        nums = defaultdict(set)
        for i,x in enumerate(A):
                nums[x].add(i)

        for x in A:
            other1 = x-K
            other2 = x+K
            if self.is_exists(nums, x, other1) \
                    or self.is_exists(nums, x, other2):
                return True
        return False


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_diffPossible_1(self):
        result = self.solution.diffPossible([1, 5, 3], 2)
        expected = True
        self.assertEqual(result, expected)


if __name__=='__main__':
    
    unittest.main()