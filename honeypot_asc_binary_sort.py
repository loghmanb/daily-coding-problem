'''
Ascending Binary Sorting

https://www.glassdoor.co.uk/Interview/Honeypot-Developer-Interview-Questions-EI_IE1281214.0,8_KO9,18.htm#InterviewReview_24340977

Sort an integer array by ascending number of 1's in each number's binary representation.
Consider an array of decimal integers. We want to rearrange the array according to the following rules:
 
    Sort the integers in ascending order by the number of 1's in their binary representations.
    Elements having the same number of 1's in their binary representations are ordered by increasing decimal value.
 
For example, consider the array [7, 8, 6, 5]10 = [0111, 1000, 0110, 0101]2.  First group the items by number of binary digits equal to 1: [[1000], [0101, 0110], [0111]]2.  The elements with two 1's now must be ordered:  [0110, 0101]2 = [6, 5]10.  We sort those two elements in ascending order by value making our final array [1000, 0101, 0110, 0111]2 = [8, 5, 6, 7]10.
 
Function Description
Complete the function rearrange in the editor below. The function must return an array of decimal integers sorted per the rules above.
 
rearrange has the following parameter(s):
    elements[elements[0],...elements[n-1]]:  an array of integers to sort
 
Constraints
    1 < n < 105
    1 < elements[i] < 109
 
Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.
 
The first line contains an integer n, the size of the integer array elements.
The next n lines each contain elements[i] where 0 &#8804; i < n.
Sample Case 0
Sample Input 0
3
1
2
3
 
Sample Output 0
1
2
3
 
Explanation 0
Given elements = [1, 2, 3]:
    (1)10 → (1)2
    (2)10 → (10)2
    (3)10 → (11)2
 
The decimal integers 1 and 2 both have one 1 in their binary representation, so we order them by increasing decimal value (i.e., 1 < 2). The decimal integer 3 has two 1's in its binary representation, so we order it after 1 and 2. We then return elements = [1, 2, 3] as our sorted array.
 
Sample Case 1
Sample Input 1
5
5
3
7
10
14
 
Sample Output 1
3
5
10
7
14
 
Explanation 1
Given elements = [5, 3, 7, 10, 14]:
    (5)10 → (101)2
    (3)10 → (11)2
    (7)10 → (111)2
    (10)10 → (1010)2
    (14)10 → (1110)2
 
The decimal integers 5, 3, and 10 have two 1's in their binary representations, so we order them by increasing decimal value (i.e., 3 < 5 < 10). The decimal integers 7 and 14 have three 1's in their binary representations, so we place them after 3, 5, and 10 in increasing decimal order (i.e., 7 < 14). We then return elements = [3, 5, 10, 7, 14] as our sorted array.
'''

import unittest

def sort_asc_binary(arr):
    arr = [(bin(x).count('1'), x) for x in arr]
    arr.sort()
    return [x[1] for x in arr]


class TestSortBinary(unittest.TestCase):

    def test_binary_asc_sort_1(self):
        result = sort_asc_binary([1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(expected, result)

    def test_binary_asc_sort_2(self):
        result = sort_asc_binary([5, 3, 7, 10, 14])
        expected = [3, 5, 10, 7, 14]
        self.assertEqual(expected, result)


if __name__ == "__main__":
    
    unittest.main()