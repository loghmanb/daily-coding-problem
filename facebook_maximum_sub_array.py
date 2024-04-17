"""
This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""
import unittest

def maximum_sub_array(arr):
    i, j, sum_arr, max_sub_arr, N = 0, 0, 0, 0, len(arr)
    while i<N:
        sum_arr += arr[j]
        if sum_arr<=0:
            i += 1
            j = i
            sum_arr = 0
        else:
            if max_sub_arr<sum_arr:
                max_sub_arr = sum_arr

            j = (j+1) % N
            if j==i:
                i += 1
                j = i
                sum_arr = 0
    return max_sub_arr


class TestDiagonalFunction(unittest.TestCase):
    
    def test_1(self):
        arr = [1, 3, 5, -4, -4, 7, 3, -3]
        self.assertEquals(maximum_sub_array(arr), 16)

    def test_2(self):
        arr = [-4, 5, 1, 0]
        self.assertEquals(maximum_sub_array(arr), 6)

    def test_3(self):
        arr = [8, -1, 3, 4]
        self.assertEquals(maximum_sub_array(arr), 15)


if __name__=='__main__':
    unittest.main()