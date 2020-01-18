'''
Rearranging a Word

https://www.glassdoor.co.uk/Interview/Honeypot-Developer-Interview-Questions-EI_IE1281214.0,8_KO9,18.htm#InterviewReview_24340977

Rearrange letters to create the next lexicographically larger string

Given two strings, one is said to be alphabetically greater than the other if its leftmost differing character is of greater ordinal value than the one in the other string. For example, abd is greater than abc because their first differing characters, d > c.
 
More formally, consider a string, word, consisting of lowercase letters, ascii[a-z]. If we permute word's characters into a new string, x, we say that x is alphabetically greater than word if the following two conditions are satisfied:
 
    The sequence of the first i-1 characters in both word and x are exactly the same.
    The ith character of string x is alphabetically greater than the ith character of word.
 
Given word, we want to find the next alphabetically greater string.
 
For example, the string word = "baca" has the following permutations:
    Alphabetically smaller strings (in ascending order): "aabc", "aacb", "abac", "abca", "acab", "acba", and "baac".
    Alphabetically greater strings (in ascending order): "bcaa", "caab", "caba", and "cbaa".
This means that the next alphabetically greater string is "bcaa".
 
Function Description

Complete the function rearrangeWord in the editor below. The function must return the next lexicographically larger permutation of the string. If no such string exists, return the string "no answer" instead.
 
rearrangeWord has the following parameter(s):
    word:  the string to analyze
 
Constraints
word[i] subset of ascii[a-z].
    2 <= |word| <=104
 
Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function.
 
The only line contains the string word.
Sample Case 0
Sample Input 0
xy
Sample Output 0
yx
Explanation 0
We can rearrange the characters in word = "xy" to create the next alphabetically greater string, so we return yx.

Sample Case 1
Sample Input 1
pp
Sample Output 1
no answer
Explanation 1
There is no way we can rearrange the characters in word = "pp" to create an alphabetically greater string, so we return no answer.

Sample Case 2
Sample Input 2
hefg
Sample Output 2
hegf
Explanation 2
We can rearrange the characters in word = "hefg" to create the next alphabetically greater string, so we return hegf.  
'''
import unittest

def rearrnging_word(word):
    if not word: return

    n = len(word)
    pre_ch = word[-1]
    for i in range(1, n):
        j = n-i-1
        if pre_ch>word[j]:
            return word[:j] + pre_ch + ''.join(sorted([word[j]]+list(word[j+2:])))
        pre_ch = word[j]
    return

class RearrangeWordTest(unittest.TestCase):

    def test_rearrnging_word_xy(self):
        result = rearrnging_word('xy')
        expected = 'yx'
        self.assertEqual(expected, result)

    def test_rearrnging_word_pp(self):
        result = rearrnging_word('pp')
        expected = None
        self.assertEqual(expected, result)

    def test_rearrnging_word_hefg(self):
        result = rearrnging_word('hefg')
        expected = 'hegf'
        self.assertEqual(expected, result)

    def test_rearrnging_word_ccdaba(self):
        result = rearrnging_word('ccdba')
        expected = 'cdabc'
        self.assertEqual(expected, result)
    

if __name__ == "__main__":
    
    unittest.main()