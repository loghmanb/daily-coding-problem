'''
This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
'''

import unittest

def find_anagram_in_str(S, W):
    ans = []
    start = 0
    word = {}
    for ch in W:
        if ch not in word:
            word[ch] = 1
        else:
            word[ch] += 1

    W = ''.join(sorted(W))
    anagrams = {}
    for i,ch in enumerate(S):
        if ch not in word:
            start = i + 1
            anagrams = {}
        elif word[ch]>anagrams.get(ch, 0):
            anagrams[ch] = anagrams.get(ch,0) + 1
            if i-start+1==len(W):
                ans.append(start)
                anagrams[S[start]] -= 1
                start += 1
        else:
            anagrams[ch] += 1
            while word[ch]<anagrams[ch]:
                anagrams[S[start]] -= 1
                start += 1
    return ans


class TestFindAnagramInString(unittest.TestCase):

    def test_find_anagram_in_str_3letter_in_string(self):
        result = find_anagram_in_str("abxaba", "ab")
        expected = [0, 3, 4]
        self.assertEquals(expected, result)


if __name__ == "__main__":
    
    unittest.main()