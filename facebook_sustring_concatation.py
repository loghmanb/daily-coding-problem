'''
Substring Concatenation
Asked in: Facebook

https://www.interviewbit.com/problems/substring-concatenation/

You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
'''

# @param A : string
# @param B : tuple of strings
# @return a list of integers
def findSubstring(A, B):
    ans = []
    n = len(B)
    l = len(B[0])
    hash_key = ''.join(sorted(B))
    l_hash = len(hash_key)
    for i in range(len(A)-l_hash+1):
        C = [A[i+j*l:i+j*l+l]for j in range(n)]
        C = ''.join(sorted(C))
        if C==hash_key:
            ans.append(i)
    return ans


if __name__=='__main__':
    data = [
        [
            ["barfoothefoobarman", ["foo", "bar"]], [0,9]
        ]
    ]
    for d in data:
        print('input', d[0], 'output', findSubstring(*d[0]))