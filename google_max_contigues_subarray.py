'''
Max Non Negative SubArray
Asked in: Google

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

Input Format:

The first and the only argument of input contains an integer array A, of length N.
Output Format:

Return an array of integers, that is a subarray of A that satisfies the given conditions.
Constraints:

1 <= N <= 1e5
1 <= A[i] <= 1e5
Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]
    
Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.

'''

def maxset(A):
    l = []
    pre_l = []
    m = -1
    pre_val = 0
    for i,x in enumerate(A):
        if x<0:
            pre_val = 0
            pre_l = []
        else:
            pre_val += x
            if pre_val>m:
                m = pre_val
                l = pre_l
            pre_l.append(x)
    return l


if __name__=='__main__':
    data = [
            [[1, 2, 5, -7, 2, 3], [1, 2, 5]]
    ]
    
    for d in data:
        print('input', d[0], 'output', maxset(d[0]))