'''
Intersection Of Sorted Arrays
Asked in:  
Facebook
Google
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]

 NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both arrays should be included multiple times in the final output.
'''

# @param A : tuple of integers
# @param B : tuple of integers
# @return a list of integers
def intersect(A, B):
    p1, p2 = 0, 0
    N1, N2 = len(A), len(B)
    ans = []
    
    while p1<N1 and p2<N2:
        if A[p1]<B[p2]:
            p1 += 1
        elif A[p1]>B[p2]:
            p2 += 1
        else:
            ans.append(A[p1])
            p1 += 1
            p2 += 1
        
    return ans


if __name__ == "__main__":
    data = [
            [
                [
                    [1, 2, 3, 3, 4, 5, 6],
                    [3, 3, 5]
                ],
                [3, 3, 5]
            ]
    ]
    for d in data:
        print('input', d[0], 'output', intersect(*d[0]))