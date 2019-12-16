'''
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

def maxSubArr(arr):
    N = len(arr)
    max_sum = 0
    group_sum = 0
    for i in range(N):
        if group_sum+arr[i]>0:
            group_sum += arr[i]
        else:
            group_sum = 0
        if max_sum<group_sum:
            max_sum = group_sum
    return max_sum

if __name__ == "__main__":
    data = [
            [
               [34, -50, 42, 14, -5, 86],
               137 
            ],
            [
                [-5, -1, -8, -9],
                0
            ]
    ]
    for d in data:
        print('input', d[0], 'output', maxSubArr(d[0]))