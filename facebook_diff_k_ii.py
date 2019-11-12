'''
Diffk II
Asked in: Facebook

https://www.interviewbit.com/problems/diffk-ii/

Given an array A of integers and another non negative integer k, 
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2

Output :

1
as 3 - 1 = 2

Return 0 / 1 for this problem.
'''

from collections import defaultdict

# @param A : tuple of integers
# @param B : integer
# @return an integer
def diffPossible(A, B):
    nums = defaultdict(set)
    for i,x in enumerate(A):
            nums[x].add(i)

    for i,x in enumerate(A):
        other = x-B
        no_of_num = len(nums[other])
        if other!=x and no_of_num>0 or no_of_num>1:
            return 1
    return 0


if __name__=='__main__':
    data = [
            [
                [[1, 5, 3], 2], 1
            ]
    ]

    for d in data:
        print('input', d[0], 'output', diffPossible(*d[0]))