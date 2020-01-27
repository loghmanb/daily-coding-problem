'''
This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
'''

import unittest

def make_palindrome(string, k):
    if k<0: return None

    N = len(string)
    mid = N//2
    i = 0
    while i<mid:
        if string[i]==string[N-i-1]:
            if i==mid-1:
                return string
            i += 1
        else:
            break
    
    inner_palindrome = []
    s = make_palindrome(string[i:N-i-1], k-1)
    if s is not None:
        inner_palindrome.append((len(s), s))
    s = make_palindrome(string[i+1:N-i], k-1)
    if s is not None:
        inner_palindrome.append((len(s), s))
    s = make_palindrome(string[i+1:N-i-1], k-2)
    if s is not None:
        inner_palindrome.append((len(s), s))
    if inner_palindrome:
        inner_palindrome.sort(reverse=True)
        return string[:i] + inner_palindrome[0][1] + string[N-i:]


class MakePalindromeTest(unittest.TestCase):

    def test_make_palindrome_1(self):
        result = make_palindrome('waterrfetawx', 2)
        expected = 'waterretaw'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    
    unittest.main()