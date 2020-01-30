'''
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]
    
Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
'''

import unittest

def maxNoneNegativeSubArray(arr):
    start = end = None
    val = -1
    i_s = i_e = None
    i_v = 0
    for i,x in enumerate(arr):
        if x>=0:
            if i_s is None:
                i_s = i_e = i
            else:
                i_e = i
            i_v += x
            if val<i_v:
                start, end, val = i_s, i_e, i_v
        else:
            i_v = 0
            i_s = i_e = None
    if start is None:
        return []
    else:
        return arr[start:end+1]


class MaxNoneNegativeSubArrayTest(unittest.TestCase):

    def test_maxNoneNegativeSubArray_1(self):
        result = maxNoneNegativeSubArray([1, 2, 5, -7, 2, 3])
        expected = [1, 2, 5]
        self.assertEqual(result, expected)

    def test_maxNoneNegativeSubArray_2(self):
        result = maxNoneNegativeSubArray([10, -1, 2, 3, -4, 100])
        expected = [100]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    
    unittest.main()