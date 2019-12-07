'''
Merge Two Sorted Lists II
Asked in: Adobe, Expedia, Microsoft

https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result. 
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input : 
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]
'''

# @param A : list of integers
# @param B : list of integers
def merge(A, B):
    iA, iB = 0, 0
        
    while iA<len(A) or iB<len(B):
        if iA>=len(A):
            A.append(B[iB])
            iB += 1
        elif iB>=len(B):
            break
        elif A[iA]<B[iB]:
            iA += 1
        else:
            A.insert(iA, B[iB])
            iB += 1
    return ' '.join(map(str, A))


if __name__ == "__main__":
    data = [
            [
                [[1, 5, 8], [6, 9]]
            ]
    ]

    for d in data:
        print('input', d[0], 'output', merge(*d[0]))