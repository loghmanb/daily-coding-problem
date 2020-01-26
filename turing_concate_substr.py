'''
Turing.com

Alice has two strings, initial and goal. She can remove some number of characters from initial, which will give her a subsequence of that string. A string with no deletions is still considered a subsequence of itself. Given these two strings, can you find the minimum number of subsequences of initial that, when appended together, will form goal?

Functions
minimumConcat() has two parameters:

initial: the source string that you will get subsequences from
goal: the target string that needs to be formed

Input Format
For some of our templates, we have handled parsing for you. If we do not provide you a parsing function, you will need to parse the input directly. In this problem, our input format is as follows:

The first line is the initial String that we will be generating subsequences from
The second line is the goal String to form
Here is an example of the raw input:

abc
bcbac

Expected Output
Return the number of minimum possible subsequences of initial that can be appended together to form goal.

If there are no possible solutions, return -1.


Constraints
Both initial and goal can only contain lowercase letters, [a - z].
Assume that the bounds of the length of the two strings are the following:
0 <= length of initial <= 100
0 <= length of goal <= 100000

Example
Example minimumConcat() Input #1

initial: "xyz"
goal: "xzyxz"
Example Output #1

3
Solution #1

Our goal can be constructed from the following subsequences of initial:

"xz" + "y" + "xz"
Example minimumConcat() Input #2

initial: "abc"
goal: "acdbc"
Example Output #2

-1
Solution #2

No subsequence of initial can construct goal, as initial does not contain the character 'd'.

'''

import unittest

def minimumConcat(initial, goal):
    res = 0
    start = i = j = 0
    while i<len(goal):
        if goal[i] == initial[j]:
            i += 1
        if j<len(initial)-1:
            j += 1
        elif start==i:
            res = -1
            break
        else:
            res += 1
            start = i
            j = 0
            
    return res
   

class MinTest(unittest.TestCase):

    def test_minimumConcat_1(self):
        result = minimumConcat('abc', 'bcbac')
        expected = 3
        self.assertEqual(result, expected)

    def test_minimumConcat_2(self):
        result = minimumConcat('abc', 'acdbc')
        expected = -1
        self.assertEqual(result, expected)

    def test_minimumConcat_3(self):
        result = minimumConcat("xyz", "xzyxz")
        expected = 3
        self.assertEqual(result, expected)


if __name__ == "__main__":
    
    unittest.main()