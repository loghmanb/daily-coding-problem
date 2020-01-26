'''
https://www.hackerrank.com/challenges/largest-permutation/problem

You are given an unordered array of unique integers incrementing from . You can swap any two elements a limited number of times. Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.

For example, if  and the maximum swaps , the following arrays can be formed by swapping the  with the other elements:

[2,1,3,4]
[3,2,1,4]
[4,2,3,1]
The highest value of the four (including the original) is . If , we can swap to the highest possible value: .

Function Description

Complete the largestPermutation function in the editor below. It must return an array that represents the highest value permutation that can be formed.

largestPermutation has the following parameter(s):

k: an integer that represents the limit of swaps
arr: an array of integers
Input Format

The first line contains two space-separated integers  and , the length of  and the maximum swaps that can be performed. The second line contains  unique space-separated integers  where .

Constraints



Output Format

Print the lexicographically largest permutation you can make with at most  swaps.
Sample Input 0

5 1
4 2 3 5 1
Sample Output 0

5 2 3 4 1
Explanation 0

You can swap any two numbers in  and see the largest permutation is 

Sample Input 1

3 1
2 1 3
Sample Output 1

3 1 2
Explanation 1

With 1 swap we can get ,  and . Of these,  is the largest permutation.

Sample Input 2

2 1
2 1
Sample Output 2

2 1
Explanation 2

We can see that  is already the largest permutation. We don't make any swaps.
'''

import unittest

from collections import defaultdict
from bisect import insort

def largestPermutation(k, arr):
    N = len(arr)
    largest_arr = sorted(arr, reverse=True)
    no_pos = defaultdict(list)
    for i,x in enumerate(arr):
        no_pos[x].append(i)
    pre_i = 0
    for _ in range(k):
        for i in range(pre_i, N):
            pre_i = i + 1
            if largest_arr[i]!=arr[i]:
                x = largest_arr[i]
                y = arr[i]
                j = no_pos[largest_arr[i]][0]
                arr[j], arr[i] = arr[i], arr[j]
                del no_pos[x][0]
                insort(no_pos[x], i)
                no_pos[y].remove(i)
                insort(no_pos[y], j)
                break
    return arr

class LargestPermutationTest(unittest.TestCase):

    def test_largestPermutation_1(self):

        result = largestPermutation(1, [4, 2, 3, 5, 1])
        expected = [5, 2, 3, 4, 1]
        self.assertEqual(expected, result)

    
if __name__ == "__main__":
    
    unittest.main()