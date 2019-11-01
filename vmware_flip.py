'''
Flip
https://www.interviewbit.com/problems/flip/

Asked in: VMWare

You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. 
In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, 
we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. 
If you don’t want to perform the operation, return an empty array. Else, return an array 
consisting of two elements denoting L and R. If there are multiple solutions, 
return the lexicographically smallest pair of L and R.

Notes:

Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,

S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Another example,

If S = 111

No operation can give us more than three 1
'''

def cmp_lexicographically(a0, a1, b0, b1):
    return (10*a0+a1) > (10*b0+b1)

# @param A : string
# @return a list of integers
def flip(A):
    max_zero = 0
    ans = [len(A)+1, len(A)+1]
    start = 0
    val = 0
    for i in range(len(A)):
        if A[i]=='1':
            if val>0:
                val -= 1
            else:
                start = i + 1
                val = 0
        else:
            val += 1
            if max_zero<=val:
                #check the lexicographically smallest pair or making better answer
                if cmp_lexicographically(ans[0], ans[1], start+1, i+1) or (max_zero<val):
                    ans = [start+1, i+1]
                max_zero = val

    return ans if ans[0]<len(A)+1 else []


if __name__=='__main__':
    data = [
            ['010', [1, 1]]
           ]
    
    for d in data:
        print('input', d[0], 'output', flip(d[0]))