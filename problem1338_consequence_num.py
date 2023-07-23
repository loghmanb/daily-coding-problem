"""
This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
import unittest

def longest_consecutive_len(arr):
    ans = 0
    s = set(arr)
    for x in s:
        k = 1
        if x-1 not in s:
            while x+1 in s:
                x += 1
                k += 1
        ans = max(ans, k)

    return ans

class TestLongConsequenceLen(unittest.TestCase):
    def test_1(self):
        arr = [100, 4, 200, 1, 3, 2]
        k = longest_consecutive_len(arr)
        self.assertEqual(k, 4)

if __name__=='__main__':
    unittest.main()