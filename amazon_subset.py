'''
Subset
Asked in: Amazon, Microsoft

https://www.interviewbit.com/problems/subset/

Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]

Solution by interviewbit
'''

# @param A : list of integers
# @return a list of list of integers
def subsets(A):
    A.sort(reverse = True)
    res = []
        
    for i in range(len(A)):
        x =  [A[i]]
        n = [x + y for y in res]
        if len(res) != 0:
            res += n
        res += [x]
            
    res.append([])
    res.reverse()
    return res


if __name__ == "__main__":
    data = [
            [
                [1,2,3],
                [
                 [],
                 [1],
                 [1, 2],
                 [1, 2, 3],
                 [1, 3],
                 [2],
                 [2, 3],
                 [3],
                ]
            ]
    ]
    for d in data:
        print('input', d[0], 'output', subsets(d[0]))