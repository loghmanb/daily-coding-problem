'''
Equal
Asked in: Facebook

https://www.interviewbit.com/problems/equal/

Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

Note:

1) Return the indices `A1 B1 C1 D1`, so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 

2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR 
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
If no solution is possible, return an empty list.
'''

from collections import defaultdict
from functools import cmp_to_key

def cmp_nums(x, y):
    if x[0]>y[0]:
        return 4
    elif x[0]==y[0] and x[1]>y[1]:
        return 3
    elif x[0]==y[0] and x[1]==y[1] and x[2]>y[2]:
        return 2
    elif x[0]==y[0] and x[1]==y[1] and x[2]==y[2] and x[3]>y[3]:
        return 1
    return -1
        
# @param A : list of integers
# @return a list of integers
def equal(A):
    ans = []
    N = len(A)
    h = defaultdict(set)
    for i in range(N):
        for j in range(i+1, N):
            k = A[i]+A[j]
            if h[k]:
                for t in h[k]:
                    if i>t[0] and i not in t and j not in t:
                        ans.append([t[0], t[1], i, j])
            else:
                h[k].add((i, j))
                    
    if not ans:
            return []
    ans.sort(key=cmp_to_key(cmp_nums))
    return ans[0]


if __name__=='__main__':
    data = [
            [[3, 4, 7, 1, 2, 9, 8], [0, 2, 3, 5]]
           ]
    for d in data:
        print('input', d[0], 'output', equal(d[0]))