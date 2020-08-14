'''
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''
import unittest

import bisect


def longest_inc_subseq_recursive(arr, minVal=None):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        if minVal is None or arr[0] > minVal:
            return 1
        else:
            return 0
    else:
        if minVal is None or arr[0] > minVal:
            return max(1+longest_inc_subseq_recursive(arr[1:], arr[0]),
                       longest_inc_subseq_recursive(arr[1:], minVal))
        else:
            return longest_inc_subseq_recursive(arr[1:], minVal)


def longest_inc_subseq_dp(arr):
    longest_sub = []
    pre_len = 0
    for i, x in enumerate(arr):
        if i == 0:
            longest_sub.append((x, i, 1))
            pre_len = 1
        else:
            idx = bisect.bisect_left(longest_sub, (x, i, 0))
            if idx > 0:
                idx -= 1
                pre_len = max(pre_len, longest_sub[idx][2]+1)
            longest_sub.insert(idx+1, (x, i, pre_len))
    return pre_len


class SolutionTestCase(unittest.TestCase):

    def test_recursive_method_1(self):
        self.assertEqual(3, longest_inc_subseq_recursive(
            [1, 2, 1, 5]))

    def test_recursive_method_2(self):
        self.assertEqual(6, longest_inc_subseq_recursive(
            [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

    def test_dp_method_1(self):
        self.assertEqual(3, longest_inc_subseq_dp(
            [1, 2, 1, 5]))

    def test_dp_method_2(self):
        self.assertEqual(6, longest_inc_subseq_dp(
            [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))


if __name__ == "__main__":

    unittest.main()
