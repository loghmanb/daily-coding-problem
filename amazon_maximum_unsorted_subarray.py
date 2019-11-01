'''
Maximum Unsorted Subarray

Asked in: Amazon

https://www.interviewbit.com/problems/maximum-unsorted-subarray/

You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

Example :

Input 1:

A = [1, 3, 2, 4, 5]

Return: [1, 2]

Input 2:

A = [1, 2, 3, 4, 5]

Return: [-1]
In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
'''

# @param A : list of integers
# @return a list of integers
def subUnsort( A):

    n = len(A)
    B = sorted(A)
    left = None
    right = None
    ans = [-1]
        
    for i in range(n):
        if A[i]!=B[i] and left is None:
            left = i
        if A[n-i-1]!=B[n-i-1] and right is None:
            right = n-i-1
        if left is not None and right is not None:
            ans = [left, right]
            break
        
    return ans


if __name__ == "__main__":
    data = [
            [[1, 3, 2, 4, 5], [1, 2]],
            [[1, 2, 3, 4, 5], [-1]],
           ]

    for d in data:
        print('input', d[0], 'output', subUnsort(d[0]))