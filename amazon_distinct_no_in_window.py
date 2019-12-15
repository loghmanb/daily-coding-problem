'''
Distinct Numbers in Window
Asked in: Amazon

https://www.interviewbit.com/problems/distinct-numbers-in-window/

You are given an array of N integers, A1, A2 ,…, AN and an integer K. Return the of count of distinct numbers in all windows of size K.

Formally, return an array of size N-K+1 where i’th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.

Note:

 If K > N, return empty array.
 A[i] is a signed integer
For example,

A=[1, 2, 1, 3, 4, 3] and K = 3

All windows of size K are

[1, 2, 1]
[2, 1, 3]
[1, 3, 4]
[3, 4, 3]

So, we return an array [2, 3, 3, 2].
'''

# @param A : list of integers
# @param B : integer
# @return a list of integers
def dNums(A, K):
    N = len(A)
    if K>N: return []
        
    ans = []
    q = {}
    for i in range(N):
        q[A[i]] = q.get(A[i], 0)+1
        if i+1>=K:
            if i>=K:
                if q[A[i-K]]>1:
                    q[A[i-K]] -= 1
                else:
                    del q[A[i-K]]
            ans.append(len(q.keys()))
    return ans


if __name__ == "__main__":
    data = [
            [[[1, 2, 1, 3, 4, 3], 3], [2, 3, 3, 2]]
    ]
    for d in data:
        print('input', d[0], 'output', dNums(*d[0]))