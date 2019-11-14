'''
Longest Common Prefix
Asked in:   Google

https://www.interviewbit.com/problems/longest-common-prefix/

Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
and S2.

For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Input Format

The only argument given is an array of strings A.
Output Format

Return longest common prefix of all strings in A.
For Example

Input 1:
    A = ["abcdefgh", "aefghijk", "abcefgh"]
Output 1:
    "a"
    Explanation 1:
        Longest common prefix of all the strings is "a".

Input 2:
    A = ["abab", "ab", "abcd"];
Output 2:
    "ab"
    Explanation 2:
        Longest common prefix of all the strings is "ab".
'''

# @param A : list of strings
# @return a strings
def longestCommonPrefix(A):
    N = len(A)
    M = len(A[0])
    if N==0: return ''
    elif N==1: return A[0]
    s = ''
    i = 0
    while i<M:
        ch = A[0][i]
        for j in range(1, N):
            if len(A[j])<=i or A[j][i]!=ch:
                return s
        s += ch
        i += 1
    return s


if __name__ == "__main__":
    data = [
            [["abcdefgh", "aefghijk", "abcefgh"], "a"]
    ]
    for d in data:
        print('input', d[0], 'output', longestCommonPrefix(d[0]))