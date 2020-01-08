'''
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
'''

def contiguous_sum(arr, K):
    start, total = 0, 0
    for i,x in enumerate(arr):
        total += x
        if total>K:
            while total>K:
                total -= arr[start]
                start += 1
        if total==K:
            return arr[start:i+1]
    return []

if __name__ == "__main__":
    data = [
            [
             [[1, 2, 3, 4, 5], 9],
             [2, 3, 4]
            ]
        ]
    for d in data:
        print('input', d[0], 'output', contiguous_sum(*d[0]))