"""

4366

295

Add to List

Share
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

"""

import unittest

class RemoveDuplicateLetterTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()

        assert solution.removeDuplicateLetters("acbacdcbc")=="abcd"


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_occ = {}
        stack = []
        
        for i in range(len(s)):
            last_occ[s[i]] = i

        for i in range(len(s)):
        
            if s[i] not in stack:
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    stack.pop()

                stack.append(s[i])
                
        return ''.join(stack)




if __name__ =="__main__":
    unittest.main()
    