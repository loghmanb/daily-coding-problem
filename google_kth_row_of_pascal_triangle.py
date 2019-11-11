'''
https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/

Kth Row of Pascal's Triangle

Asked in: Google

Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
Note:Could you optimize your algorithm to use only O(k) extra space?

Solution by: https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
'''

def solve(A):
    if A == 0:
        return [1]
    x = [1] * (A + 1)
    for i in range(1, A):
        x[i] = x[i - 1] * (A + 1 - i) // i
    return x


if __name__=='__main__':
    data = [ [3, [1,3,3,1]] ]
    for d in data:
        print('input', d[0], 'output', solve(d[0]))