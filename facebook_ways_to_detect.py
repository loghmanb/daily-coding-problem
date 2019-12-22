'''
Ways to Decode
Asked in: Facebook, Amazon

https://www.interviewbit.com/problems/ways-to-decode/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.



Input Format:

The first and the only argument is a string A.
Output Format:

Return an integer, representing the number of ways to decode the string.
Constraints:

1 <= length(A) <= 1e5
Example :

Input 1:
    A = "8"

Output 1:
    1

Explanation 1:
    Given encoded message "8", it could be decoded as only "H" (8).

    The number of ways decoding "8" is 1.

Input 2:
    A = "12"

Output 2:
    2

Explanation 2:
    Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
    
    The number of ways decoding "12" is 2.

DP version solved by interviewbit.com
'''

def numDecodings_recursive(A):
    if not A or A[0]=='0':
        return 0
    elif len(A)==1:
        return 1
    elif len(A)==2:
        return int(A)<=26 and 2 or 1
    ans = numDecodings_recursive(A[1:])
    if numDecodings_recursive(A[:2]):
        ans += numDecodings_recursive(A[2:])
    return ans


# @param A : string
# @return an integer
def numDecodings(A):
    d = [0]*(len(A)+1)
    d[0] = d[1] = 1
    for i in range(1,len(A)):
        no = int(A[i-1]+A[i])
        if A[i]=='0' and(no!=10 and no!=20) :
            return 0
        elif no==10 or no==20 :
            d[i+1] = d[i-1]
        elif no>10 and no<=26 :
            d[i+1] = d[i]+d[i-1]
        else: 
            d[i+1] = d[i]
    return d[-1]


if __name__ == "__main__":
    data = [
            ['1213', 25]
    ]
    for d in data:
        print('input', d[0], 'output#1', numDecodings(d[0]), 'output#2', numDecodings_recursive(d[0]))

