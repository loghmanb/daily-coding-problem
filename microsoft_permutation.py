'''
Permutations
Asked in: Microsoft, Adobe, Google

https://www.interviewbit.com/problems/permutations/

Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points. 
'''
# @param A : list of integers
# @return a list of list of integers
def permute(A):
    if not A: return []
    elif len(A)==1: return [A]
        
    ans = []
    for i in range(len(A)):
        l = permute(A[:i]+A[i+1:])
        for x in l:
            ans.append([A[i]]+x)
    return ans


if __name__ == "__main__":
    data = [
            [
                [1, 2, 3],
                [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            ]
    ]
    for d in data:
        print('input', d[0], 'output', permute(d[0]))