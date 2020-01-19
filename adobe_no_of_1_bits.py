'''
Number of 1 Bits

Asked in: Adobe, Yahoo

https://www.interviewbit.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

Note that since Java does not have unsigned int, use long for Java
'''

import unittest


class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        no_of_one = 0
        while A>0:
            no_of_one += A%2
            A = A//2
        return no_of_one


    # @param A : integer
    # @return an integer
    def numSetBitsByFunc(self, A):
        return bin(A).count('1')


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_numSetBits_5(self):
        result = self.solution.numSetBits(5)
        expected = 2
        self.assertEqual(result, expected)

    def test_numSetBitsByFunc_5(self):
        result = self.solution.numSetBitsByFunc(5)
        expected = 2
        self.assertEqual(result, expected)


if __name__ == "__main__":
    
    unittest.main()