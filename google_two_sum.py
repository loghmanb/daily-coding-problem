'''
2 Sum
Asked in: Facebook, Amazon, Google

https://www.interviewbit.com/problems/2-sum/

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
'''

def twoSum(A, B):
    d = {}
    l = []
    for i,x in enumerate(A):
        if x not in d:
            d[x] = []
        d[x].append(i+1)
    for i,x in enumerate(A):
        if (B-x) in d:
            i1 = i+1
            i2 = d[B-x][0]
            if i1==i2:
                if len(d[B-x])>1:
                    i2 = d[B-x][1]
                else:
                    continue
            if i2<i1:
                break
            l.append([i1, i2])
    l = sorted(l, key=lambda x:(x[1],x[0]))
    return l and l[0] or []


if __name__=='__main__':
    data = [
        [[[2, 7, 11, 15], 9], [1, 2]]
    ]
    for d in data:
        print('input', d[0], 'output', twoSum(*d[0]))