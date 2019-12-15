'''
4 Sum
Asked in: Amazon, Google

https://www.interviewbit.com/problems/4-sum/

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

 Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
Example :
Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:

    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    (-1,  0, 0, 1)
Also make sure that the solution set is lexicographically sorted.
Solution[i] < Solution[j] iff Solution[i][0] < Solution[j]

Solved by interviewbite.com
'''

# @param A : list of integers
# @param B : integer
# @return a list of list of integers
def fourSum(arr, target):
    res = set()
    if not arr: return res

    arr.sort()
    N = len(arr)
    twoSum = {}

    for i in range(N):
        for j in range(i+1, N):
            sum_of_two_num = arr[i] + arr[j]
            if target-sum_of_two_num in twoSum:
                for k,l in twoSum[target-sum_of_two_num]:
                    if i>l:
                        res.add((arr[k], arr[l], arr[i], arr[j]))
            
            if sum_of_two_num not in twoSum:
                twoSum[sum_of_two_num] = set()
            twoSum[sum_of_two_num].add( (i, j) )
    res = list(res)
    res.sort()
    return res


if __name__ == "__main__":
    data = [
            [
                [[1, 0, -1, 0, -2, 2], 0],
                [
                    (-2, -1, 1, 2),
                    (-2,  0, 0, 2),
                    (-1,  0, 0, 1),
                ]
            ]
    ]
    for d in data:
        print('input', d[0], 'output', fourSum(*d[0]))