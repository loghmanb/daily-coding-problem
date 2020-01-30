'''
Max Sum Contiguous Subarray
https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

Asked in: Facebook, Paypal, Yahoo, Microsoft, LinkedIn, Amazon, Goldman Sachs

Find the contiguous subarray within an array, A of length N which has the largest sum.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:

1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:

Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
'''

import unittest

def maxSubArray(A):
    if not A: return
    
    max_subA = A[0]
    subA = 0
    for i,x in enumerate(A):
        if i==0: 
            subA = x
        elif subA>0 and (x+subA)>0:
            subA += x
        else:
            subA = x
        if max_subA<subA:
            max_subA = subA
    return max_subA


class MAxContSubArrTest(unittest.TestCase):

        def test_maxSubArray_1(self):
            result = maxSubArray([1, 2, 3, 4, -10])
            expected = 10
            self.assertEqual(result, expected)

        def test_maxSubArray_2(self):
            result = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            expected = 6
            self.assertEqual(result, expected)


if __name__=='__main__':
    
    unittest.main()