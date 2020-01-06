'''
https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/
Largest Continuous Sequence Zero Sum
Asked in: Microsoft
Find the largest continuous sequence in a array which sums to zero.

Example:

Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}

Hint:
Lets try to reduce the problem to a much simpler problem.
Lets say we have another array sum where

  sum[i] = Sum of all elements from A[0] to A[i]
Note that in this array, sum of elements from A[i] to A[j] = Sum[j] - Sum[i-1]

We need to find j and i such that sum of elements from A[i] to A[j] = 0
 Or Sum[j] - Sum[i-1] = 0
 Or Sum[j] = Sum[i-1]

 Solved by interviewbit.com

'''

def lszero(A):
    d = {A[0]:0}
    m = 0
    s = 0
    l = 0
    i_start = -1
    i_end = -1
    for i,x in enumerate(A):
        s += x
        if s==0 and s not in d:
            d[0] = 0
        if s in d:
            l = (i-d[s]+1)
            if s==0: l+=1
            if l>m:
                m = l
                i_start = d[s]
                if s!=0:
                    i_start+=1
                i_end = i+1
        else:
            d[s] = i
    if i_start<0:
        return []
    return A[i_start:i_end]


if __name__=='__main__':
    d = [
         [[-1, 3, 4, -5, 2, 6], []],
         [[1, 2, -3, 3], [ 1, 2, -3]],
         [[1 ,2 ,-2 ,4 ,-4], [2 ,-2 ,4 ,-4]],
    ]

    for l in d:
        print('input', l[0], 'output', lszero(l[0]))