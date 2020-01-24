'''
This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
'''

import unittest

def find_shortest_substr(string, special_lettets):
    special_lettets = set(special_lettets)
    start = 0
    letters = {}
    shortest_substr = None
    for i,ch in enumerate(string):
        if ch in special_lettets:
            if ch not in letters:
                letters[ch] = 1
            else:
                letters[ch] += 1
        if len(letters)==0:
            start = i+1
        elif len(letters.keys())== len(special_lettets):
            if shortest_substr is None \
                    or i-start+1<len(shortest_substr):
                shortest_substr = string[start:i+1]
            if len(special_lettets)==1:
                start = i+1
            else:
                while len(letters.keys())>=len(special_lettets)-1:
                    ch = string[start]
                    if len(letters)==len(special_lettets) and \
                            i-start+1<len(shortest_substr):
                        shortest_substr = string[start:i+1]
                    if ch in letters:
                        letters[ch] -= 1
                        if letters[ch]==0:
                            del letters[ch]
                    start += 1
                start -= 1
                letters[string[start]] = 1
    return shortest_substr


class FindShortestSubstr(unittest.TestCase):
    
    def test_find_shortest_substr_1(self):

        result = find_shortest_substr("figehaeci", {'a', 'e', 'i'})
        expected = "aeci"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    
    unittest.main()
