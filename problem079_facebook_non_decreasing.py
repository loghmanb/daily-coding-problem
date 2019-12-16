'''
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
'''

def nonDecreasingable(arr):
    if len(arr)<2: return True

    noOfChanges = 0
    min1 = min2 = arr[0] 
    for i in range(1, len(arr)):
        if arr[i]<min2:
            noOfChanges += 1
            if arr[i]>=min1:
                min2 = arr[i]
            if noOfChanges>1:
                return False
        else:
            min1 = min2
            min2 = arr[i]
    return True

if __name__ == "__main__":
    data = [
            [
                [4, 10, 3, 11, 12], True,
            ],
            [
                [4, 10, 4, 5, 6], True,
            ],
            [
                [4, 10, 4, 3, 6], False,
            ],
    ]
    for d in data:
        print('input', d[0], 'output', nonDecreasingable(d[0]))