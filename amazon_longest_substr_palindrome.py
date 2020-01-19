'''
Longest Palindarome Substring

https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

Asked by: Amazon

Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana"

Solved by dynamic programming or recursive functions

if S is palindarome so reteurn len of S
else check for S[1:] or S[:-1]

if len of S is equal 1 so return 1 (because of each character is palindarome)
if len of S is equal 2 and S[0]==S[1] return 2 

'''

import unittest

def longestPalindromeSubstring(S):
    if not S: return 0
    
    N = len(S)
    table = [[False]*N for _ in range(N)]
    
    start = 0
    maxLen = 1
    
    #Check for single char and double contigues chars
    for i in range(N):
        #Each character is palindarome
        table[i][i] = True
        if i<N-1:
            #Check for two characters
            if S[i]==S[i+1]:
                table[i][i+1] = True
                start = i
                maxLen = 2

    #Check for 3 and more charachters
    for k in range(3, N+1):
        for i in range(N+1-k):
            #find mirror position of i
            j = i + k - 1
            #str[i:j] is palindarome if str[i+1:j-1] is palindarome and str[i] is equal to str[j]
            if table[i+1][j-1] and S[i]==S[j]:
                table[i][j] = True
                if maxLen<k:
                    maxLen = k
                    start = i
    
    palindrome_sub_str = S[i:i+maxLen]

    return maxLen


class PalindromeSubStrTest(unittest.TestCase):

    def test_longestPalindromeSubstring_baab(self):
        result = longestPalindromeSubstring("baab")
        expected = 4
        self.assertEqual(expected, result)

    def test_longestPalindromeSubstring_aabcdcb(self):
        result = longestPalindromeSubstring("aabcdcb")
        expected = 5
        self.assertEqual(expected, result)


if __name__ == "__main__":
    
    unittest.main()