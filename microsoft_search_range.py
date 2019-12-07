'''
Search for a Range
Asked in: Google, Microsoft

https://www.interviewbit.com/problems/search-for-a-range/

Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].

Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

 Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
Constraints

1 <= N <= 10^6
1 <= A[i], B <= 10^9
For Example

Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]
'''

# @param A : tuple of integers
# @param B : integer
# @return a list of integers
def searchRange(A, B):
    start, end = 0, len(A)-1
    while start<end:
        mid = (start + end) // 2
        if mid==start: break
        if A[mid]>B:
            end = mid
        elif A[mid]<B:
            start = mid
        else:
            break
        
    if start<end:
        if A[start]<B:
            i = mid
            while A[i]==B and i>start:
                i -= 1
            start = (i+1) if A[i+1]==B else -1
                
        if A[end]>B:
            i = mid
            while A[i]==B and i<end:
                i += 1
            end = (i-1) if A[i-1]==B else -1

    if A[start]!=B and A[end]!=B:
        start = end = -1

    return [start, end]


if __name__ == "__main__":
    data = [
             [
              [[5, 7, 7, 8, 8, 10], 8],
              [3, 4]
             ]
    ]

    for d in data:
        print('input', d[0], 'output', searchRange(*d[0]))