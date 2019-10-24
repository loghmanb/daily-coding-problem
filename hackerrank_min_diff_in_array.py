'''
Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, 
but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements 
have the smallest absolute difference between them.

For example, if you've got the list [5, 2, 3, 4, 1], sort it as [1, 2, 3, 4, 5] to see that several pairs 
have the minimum difference of 1: [(1, 2), (2, 3), (3, 4), (4, 5)]. 
The return array would be [1, 2, 2, 3, 3, 4, 4, 5].

Given a list of unsorted integers, , find the pair of elements that have the smallest absolute difference between them. 
If there are multiple pairs, find them all.

'''

def closestNumbers(arr):
    arr = sorted(list(set(arr)))
    m = None
    ans = []
    for i in range(1, len(arr)):
        diff = arr[i]-arr[i-1]
        if m is None or m>diff:
            ans = [arr[i-1], arr[i]]
            m = diff
        elif m==diff:
            ans.append(arr[i-1])
            ans.append(arr[i])
    return ans


if __name__ == '__main__':
    data = [
            [5, 2, 3, 4, 1],
            ]
        
    for l in data:
        print(closestNumbers(l))