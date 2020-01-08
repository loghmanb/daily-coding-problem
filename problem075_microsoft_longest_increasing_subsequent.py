'''
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''
import bisect

def longest_increasing_subseq(arr, i=0, minVal=None):
    if i>=len(arr)-1:
        return 0
    
    l1 = 0
    j = i
    if minVal is not None:
        while j<len(arr)-1 and arr[j]<minVal:
            j += 1
    if j<=len(arr)-1:
        l1 = 1+longest_increasing_subseq(arr, j+1, arr[j])
    l2 = longest_increasing_subseq(arr, i+1, minVal)
    return max(l1, l2)


def longest_inc_subseq(arr):
    longest_sub = []
    pre_len = 0
    for i,x in enumerate(arr):
        if i==0:
            longest_sub.append((x, i, 1))
            pre_len = 1
        else:
            idx = bisect.bisect_left(longest_sub, (x, i, 0))
            if idx>0: 
                idx -= 1
                pre_len = max(pre_len, longest_sub[idx][2]+1)
            longest_sub.insert(idx+1, (x, i, pre_len))
    return pre_len

if __name__ == "__main__":
    data = [
            [[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6]
    ]
    for d in data:
        print('input', d[0], 'output#1', longest_increasing_subseq(d[0]), 'output#2', longest_inc_subseq(d[0]))