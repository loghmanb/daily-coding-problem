'''
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
'''

def isPartitionable(arr):
    N = len(arr)
    total = sum(arr)
    if total%2==1:
        return False
    total //= 2
    arr = sorted(arr)

    for i in range(N):
        if arr[N-1-i]<=total:
            total -= arr[N-1-i]
    
    return bool(total==0)


if __name__ == "__main__":
    data = [
            [[15, 5, 20, 10, 35, 15, 10], True]
    ]
    for d in data:
        print('input', d[0], 'output', isPartitionable(d[0]))
    