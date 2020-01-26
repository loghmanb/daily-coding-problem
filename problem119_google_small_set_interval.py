'''
This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
'''

import unittest

IN = -1
OUT = 1

def smallest_interval(arr):
    in_out = []
    for i,x in enumerate(arr):
        in_out.append((x[0], IN))
        in_out.append((x[1], OUT))
    in_out.sort()

    N = len(in_out)
    # find start/end
    start = end = None
    for i in range(N):
        if start is None and in_out[i][1]==OUT:
            start = in_out[i][0]
        if end is None and in_out[N-i-1][1]==IN:
            end = in_out[N-i-1][0]
        if start is not None and end is not None:
            break
    return [start, end]


class SmallestIntervalTest(unittest.TestCase):

    def test_smallest_interval_1(self):
        result = smallest_interval([[0, 3], [2, 6], [3, 4], [6, 9]])
        expected = [3, 6]
        self.assertEqual(result, expected)


if __name__ == "__main__":

    unittest.main()