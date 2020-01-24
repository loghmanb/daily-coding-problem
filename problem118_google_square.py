'''
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
'''

import unittest
import bisect


def square_in_list(arr):
    res = []
    for x in arr:
        bisect.insort(res, x*x)
    return res


class SquareInListTest(unittest.TestCase):

    def test_square_in_list_1(self):
        result = square_in_list([-9, -2, 0, 2, 3])
        expected = [0, 4, 4, 9, 81]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    
    unittest.main()