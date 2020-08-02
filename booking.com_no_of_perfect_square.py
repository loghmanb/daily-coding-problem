'''
Booking.com Interview Question for Software Engineer / Developers

https://www.careercup.com/question?id=5739532692488192

Given number N, Find the least number of perfect square number sum needed to get N.

Example : 
n=5 (4+1) i.e. 2
n=7 (4+1+1+1) i.e. 4
n=12 (4+4+4) i.e 3
n=20 (16+4) i.e. 2
'''

import math
import sys
import unittest

def find_no_of_perfect_square(n):
    if n<0:
        return sys.maxsize
    if n<4:
        return n
    elif n==4:
        return 1
    
    root = int(math.sqrt(n))
    if root>=2:
        return min(
            1+find_no_of_perfect_square(n-pow(root, 2)),
            n//pow(root-1,2) + find_no_of_perfect_square(n%pow(root-1,2))
        )
    else:
        return n


class NoOfPerfectSquareTextCase(unittest.TestCase):
    def test_5(self):
        self.assertEqual(2, find_no_of_perfect_square(5))

    def test_7(self):
        self.assertEqual(4, find_no_of_perfect_square(7))

    def test_12(self):
        self.assertEqual(3, find_no_of_perfect_square(12))

    def test_20(self):
        self.assertEqual(2, find_no_of_perfect_square(20))


if __name__=='__main__':
    unittest.main()