'''
Interleaving Strings
Asked in: Google, Yahoo

https://www.interviewbit.com/problems/interleaving-strings/

Given A, B, C, find whether C is formed by the interleaving of A and B.

Input Format:*

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains a string, C.
Output Format:

Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:

1 <= length(A), length(B), length(C) <= 150
Examples:

Input 1:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbcbcac"

Output 1:
    1
    
Explanation 1:
    "aa" (from A) + "dbbc" (from B) + "bc" (from A) + "a" (from B) + "c" (from A)

Input 2:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbbaccc"

Output 2:
    0

Explanation 2:
    It is not possible to get C by interleaving A and B.
'''

# @param A : string
# @param B : string
# @param C : string
# @return an integer
def isInterleave(A, B, C):
    if not C: return 1
    if len(C)!=len(A)+len(B): return 0
        
    if A and A[0]==C[0] and isInterleave(A[1:], B, C[1:]) or \
            B and B[0]==C[0] and isInterleave(A, B[1:], C[1:]):
        return 1
    return 0


if __name__ == "__main__":
    data = [
            [
                ['aabbcd','cdbaac', 'cdaababbacdc']
            ]
    ]
    for d in data:
        print('input', d[0], 'output', isInterleave(*d[0]))