'''
INVERSIONS

https://www.interviewbit.com/problems/inversions/

Given an array A, count the number of inversions in the array.

Formally speaking, two elements A[i] and A[j] form an inversion if A[i] > A[j] and i < j

Example:

A : [2, 4, 1, 3, 5]
Output : 3
as the 3 inversions are (2, 1), (4, 1), (4, 3).

Solved by interviewbit!
'''

import bisect

# @param A : list of integers
# @return an integer
def countInversions(A):
    inversions = 0
    if len(A):
        seen = [ A[0] ]
        for i in range(1, len(A)):
            if A[i] < seen[-1]:
                p = bisect.bisect(seen, A[i])
                seen.insert(p, A[i])
                inversions += i - p
            else:
                seen.append(A[i])
    return inversions


if __name__ == "__main__":
    data = [
            [
                [2, 4, 1, 3, 5],
                3
            ]
    ]
    for d in data:
        print('input', d[0], 'output', countInversions(d[0]))