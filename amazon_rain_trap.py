'''
Rain Water Trapped
Asked in: Qualcomm,Amazon

https://www.interviewbit.com/problems/rain-water-trapped/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Input Format

The only argument given is integer array A.
Output Format

Return the total water it is able to trap after raining..
For Example

Input 1:
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
Output 1:
    6
Explaination 1: <img src="http://i.imgur.com/0qkUFco.png">
    
    In this case, 6 units of rain water (blue section) are being trapped.
'''

# @param A : tuple of integers
# @return an integer
def trap(A):
    ans = 0
    N = len(A)
    B = [0]*N
    C = [0]*N
        
    B[0], C[N-1] = A[0], A[N-1]
    for i in range(1, N):
        B[i] = max(B[i-1], A[i])
        C[N-1-i] = max(C[N-i], A[N-1-i])

    for i in range(N):
        ans += min(B[i], C[i])-A[i]
    return ans


#solution by interviewbit
# @param A : tuple of integers
# @return an integer
def trap_by_stack(A):
    # Visits each element of the array A twice
    # (stacking and popping).
    # If the stack is implemented in a more basic
    # form and stack[0] is not a fast operation,
    # we could store the current maximal element
    # separately.
    stack = []
    water = 0
    for a in A:
        if stack and stack[0]<=a:
            h = stack[0]
            while stack:
                water += h-stack.pop()
        stack.append(a)
    h = stack.pop()
    while stack:
        n = stack.pop()
        if n > h:
            h = n
            continue
        water += h-n
    return water


if __name__ == "__main__":
    data = [
            [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6]
    ]
    for d in data:
        print('input', d[0], 'output#1', trap(d[0]), 'output#2', trap_by_stack(d[0]))