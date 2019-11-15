'''
Rearrange Array
Asked in: Facebook

https://www.interviewbit.com/problems/rearrange-array/

Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer

Solution:
------------
A = B + C*n
B = A % n
C = A // n
'''

# @param A : list of integers
# Modify the array A which is passed by reference. 
# You do not need to return anything in this case. 
def arrange(A):
    n = len(A)
    for i in range(len(A)):
        A[i] += (A[A[i]]%n)*n
    for i in range(len(A)):
        A[i] = A[i]//n
    return A


if __name__ == "__main__":
    data = [
            [[1, 3, 2, 0], [3, 0, 2, 1]]
    ]
    for d in data:
        arr = d[0][:]
        print('input', arr, 'output', arrange(d[0]))