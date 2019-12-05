'''
Square Root of Integer
Asked in: Facebook, Amazon, Microsoft

https://www.interviewbit.com/problems/square-root-of-integer/

Given an integar A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY



Input Format

The first and only argument given is the integer A.
Output Format

Return floor(sqrt(A))
Constraints

1 <= A <= 10^9
For Example

Input 1:
    A = 11
Output 1:
    3

Input 2:
    A = 9
Output 2:
    3
'''

# @param A : integer
# @return an integer
def sqrt(A):
    if A==0: return 0
    elif A<4: return 1
        
    start = 0
    end = A
        
    while start<end:
        mid = (start+end)//2
        if mid==start: 
            break
        val = mid*mid
        if val==A:
            start = end = mid
        elif val>A:
            end = mid
        else:
            start = mid
        
    return min(start, end)


if __name__ == "__main__":
    data = [
            [9, 3],
            [11, 3],
            [15, 3],
            [16, 4],
    ]

    for d in data:
        print('input', d[0], 'output', sqrt(d[0]))