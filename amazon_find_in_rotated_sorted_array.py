'''
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''

def find(arr, x):
    start = 0
    end = len(arr)-1
    while start<end:
        mid = (start+end)//2
        if mid==start or mid==end:
            break
        if arr[start]>arr[end]:
            if x>arr[mid]:
                if arr[mid]>arr[start]:
                    end = mid
                else:
                    start = mid
            else:
                if arr[mid]>arr[end]:
                    start = mid
                else:
                    end = mid
        else:
            if arr[mid]>x:
                end = mid
            else:
                start = mid
        if arr[start]==x:
            return start
        elif arr[end]==x:
            return end
    return -1


if __name__=='__main__':
    data = [
            [[[13, 18, 25, 2, 8, 10], 8], 4]
    ]

    for d in data:
        print('input', d[0], 'output', find(*d[0]))