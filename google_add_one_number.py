'''
Add One To Number
Asked in: Google, Microsoft

https://www.interviewbit.com/problems/add-one-to-number/

Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
'''

def plusOne(self, A):
    A[-1] += 1
    for i in range(len(A)-1, -1, -1):
        if A[i]>=10:
            A[i] = 0
            if i==0:
                A.insert(0, 1)
            else:
                A[i-1] += 1
        else:
            break
    i = 0
    while A[i]==0:
        i += 1

    return A[i:]


if __name__=='__main__':
    d = [
        [[1, 2, 3], [1, 2, 4]]
    ]

    for d in data:
        print('input', d[0], 'output', plusOne(d[0]))