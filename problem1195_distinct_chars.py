"""
Given a string, find the length of the smallest window that contains every distinct character. 
Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""

import unittest

def distinct_chars(s):
    d_chars = set()
    start = 0
    ans = 0
    for i, _ in enumerate(s):
        if s[i] not in d_chars:
            d_chars.add(s[i])
            ans = max(ans, i+1-start)
        else:
            while s[start]!=s[i]:
                d_chars.remove(s[start])
                start += 1
            start += 1
    return ans
    
class TestDistinctCharsLen(unittest.TestCase):
    def test_jujitsu(self):
        self.assertEqual(distinct_chars("jujitsu"), 5)

if __name__=='__main__':
    unittest.main()