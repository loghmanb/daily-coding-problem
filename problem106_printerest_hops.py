'''
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
'''

def can_reach_to_last(arr):
    idx = 0
    while idx < len(arr) and arr[idx]:
        idx += arr[idx]
    return bool(idx >= len(arr)-1)

if __name__ == "__main__":
    data = [
            [[2, 0, 1, 0], True],
            [[1, 1, 0, 1], False],
    ]
    for d in data:
        print('input', d[0], 'output', can_reach_to_last(d[0]))