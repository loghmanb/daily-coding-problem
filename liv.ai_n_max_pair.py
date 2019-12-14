'''
N max pair combinations
Asked in: Liv.ai

https://www.interviewbit.com/problems/n-max-pair-combinations/

Problem Setter: dhruvi Problem Tester: ganeshk2
Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6), 
9    (3+6),
9    (4+5),
8    (2+6)

Solved by Interviewbit.com
'''

import heapq

# @param A : list of integers
# @param B : list of integers
# @return a list of integers
def solve(A, B):
    N = len(A)
    visited = set()
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    result = []
    heap = []
    visited.add((0, 0))
    heapq.heappush(heap, (-(A[0] + B[0]), (0, 0)))
    for _ in range(N):
        sum_, (iA, iB) = heapq.heappop(heap)
        result.append(-sum_)
            
        tuple1 = (iA + 1, iB)
        if iA < N - 1 and tuple1 not in visited:
            heapq.heappush(heap, (-(A[iA + 1] + B[iB]), tuple1))
            visited.add(tuple1)
            
        tuple2 = (iA, iB + 1)
        if iB < N - 1 and tuple2 not in visited:
            heapq.heappush(heap, (-(A[iA] + B[iB + 1]), tuple2))
            visited.add(tuple2)
                
    return result


if __name__ == "__main__":
    data = [
            [
                [[1, 4, 2, 3], [2,5,1,6]],
                [10, 9, 9, 8],
            ]
    ]
    for d in data:
        print('input', d[0], 'output', solve(*d[0]))