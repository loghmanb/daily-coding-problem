'''
Max Distance
Asked in: Google, Amazon, Microsoft

https://www.interviewbit.com/problems/max-distance/

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)

Solution:
https://medium.com/solvingalgo/solving-algorithmic-problems-max-distance-in-an-array-7e8c9f71c8b

'''

import unittest

def maximumGap(A):
    if not A: return -1
    if len(A)==1: return 0
        
    n = len(A)
    B = []
        
    #make a new array with value,index pair
    for i,x in enumerate(A):
        B.append((x, i))
            
    B = sorted(B)

    maxIndex = float('-inf')
    rightMax = [0]*n
    for i in range(n-1, -1, -1):
        maxIndex = max(maxIndex, B[i][1])
        rightMax[i] = maxIndex

    maxGap = 0
    for i in range(n):
        maxGap = max(maxGap, rightMax[i]-B[i][1])
            
    return maxGap


class TestMaximumGap(unittest.TestCase):

    def test_maximumGap_1(self):
        result = maximumGap([3, 5, 4, 2])
        expected = 2
        self.assertEqual(expected, result)

    def test_maximumGap_2(self):
        result = maximumGap([3, 15, 2, 4, 8, 12, 6])
        expected = 6
        self.assertEqual(expected, result)

if __name__=='__main__':
    
    unittest.main()