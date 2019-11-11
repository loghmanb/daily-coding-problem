'''
Noble Integer

https://www.interviewbit.com/problems/noble-integer/

Given an integer array, find if an integer p exists in the array 
such that the number of integers greater than p in the array equals to p

If such an integer is found return 1 else return -1.
'''

# @param A : list of integers
# @return an integer
def solve(A):
    N = len(A)
    A = sorted(A)
    for i in range(N):
        if i<N-1:
            if A[i]<A[i+1]:
                if A[i]==N-i-1:
                    return 1
                elif A[i]>N-i-1:
                    break
        elif A[i]==0:
                return 1
    return -1


if __name__ == "__main__":
    data = [
            [[-6, -1, 0, -4, -3], 1],
            [[5, 4, 3, 7], 1],
        ]

    for d in data:
        print('input', d[0], 'output', solve(d[0]))