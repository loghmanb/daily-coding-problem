'''
Length of Longest Subsequence
Asked in: Microsoft

https://www.interviewbit.com/problems/length-of-longest-subsequence/

Problem Setter: mayank111 Problem Tester: glowing_glare
Given an array of integers, A of length N, find the length of longest subsequence which is first increasing then decreasing.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the answer as described in the problem statement.
Constraints:

1 <= N <= 3000
1 <= A[i] <= 1e7
Example:

Input 1:
    A = [1, 2, 1]

Output 1:
    3

Explanation 1:
    [1, 2, 1] is the longest subsequence.

Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]

Output 2:
    6
    
Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.

Solution by Interviewbit.com
'''

from bisect import bisect_left

# @param A : tuple of integers
# @return an integer
def longestSubsequenceLength(A):
    h1, h2 = [], []
    for x in A:
        i = bisect_left(h1, x)
        if i >= len(h1):
            h1.append(x)
        else: h1[i] = x

        j = bisect_left(h2, -x, len(h1) - 1) if h1 else 0
        if j >= len(h2) or len(h2) < len(h1):
            h2.append(-x)
        else:
            h2[j] = -x
    return len(h2)


if __name__ == "__main__":
    data = [
            [[1, 11, 2, 10, 4, 5, 2, 1], 6]
    ]
    for d in data:
        print('input', d[0], 'output', longestSubsequenceLength(d[0]))