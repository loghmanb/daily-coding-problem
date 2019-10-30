'''
MaxsProduct

https://www.interviewbit.com/problems/maxspprod/

You are given an array A containing N integers. 
The special product of each ith integer in this array is defined as the product of the following:

    LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j.

    RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.

Input: You will receive array of integers as argument to function.

Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9

Example:
Input: 
[2, 4, 15, 10, 8, 9, 3, 6, 4, 7]

Output:
63
'''

# @param A : list of integers
# @return an integer
def maxSpecialProduct(A):
    n = len(A)
    left = [0] * n
    right = [0] * n
    for i in range(n):
        if i>0:
            if A[i-1]>A[i]:
                left[i] = i-1
            elif A[left[i-1]]>A[i]:
                left[i] = left[i-1]
            if A[n-i-1]<A[n-i]:
                right[n-i-1] = n-i
            elif A[n-i-1]<A[right[n-i]]:
                right[n-i-1] = right[n-i]
    for i in range(n):
        ans = left[n-i-1]*right[n-i-1]
        if ans>0: return ans%1000000007
    return 0


if __name__ == "__main__":
    data = [
            [[2, 4, 15, 10, 8, 9, 3, 6, 4, 7], 63]
        ]

    for d in data:
        print('input', d[0], 'output', maxSpecialProduct(d[0]))