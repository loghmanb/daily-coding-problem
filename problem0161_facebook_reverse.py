'''
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.

'''

import unittest

def reverse_nums(arr):
    for i in range(len(arr)):
        arr[i] = not arr[i]
    return arr

class TestReverseNums(unittest.TestCase):

    def test_reverse_nums(self):
        arr = reverse_nums([31, 0, 31, 0])

if __name__ == "__main__":
    
    unittest.main() 