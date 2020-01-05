'''
Kth Smallest Element in the Array

https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/

Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element

 kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based ) 
NOTE
You are not allowed to modify the array ( The array is read only ).
Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

answer : 2
'''

# Slution #1: if you can modify array elements

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, start, end):
    pivot = arr[start]
    i, j = start+1, end

    while i<j:
        while arr[i]<pivot: i += 1
        while arr[j]>pivot: j -= 1

        if i<j: 
            swap(arr, i, j)
    
    swap(arr, start, j)

    return j


def find_kth_smallest(arr, k, start=None, end=None):
    if start is None: start = 0
    if end is None: end = len(arr)-1

    if start>end: return -1

    p = partition(arr, start, end)
    if p==k-1: 
        return arr[p]
    elif p>k-1:
        return find_kth_smallest(arr, k, start=start, end=p)
    elif p<k-1:
        return find_kth_smallest(arr, k, start=p, end=end)


#solution by using heap
import heapq

def find_kth_smallest_heap(arr, k):
    mem = arr[:k]
    heapq._heapify_max(mem)
    for i in range(k, len(arr)):
        if arr[i]<mem[0]:
            heapq._heapreplace_max(mem, arr[i])
    return mem[0]

if __name__ == "__main__":
    data = [
            [[[2, 1, 4, 3, 2], 3], 3],
    ]

    for d in data:
        print('input', d[0], 'output#1', find_kth_smallest(*d[0]), 'output#2', find_kth_smallest_heap(*d[0]))
