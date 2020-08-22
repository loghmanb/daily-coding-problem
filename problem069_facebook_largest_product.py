'''
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
'''


def largest_product(arr):
    arr = sorted(arr)
    return max(arr[-1]*arr[-2]*arr[-3], arr[0]*arr[1]*arr[-1])


if __name__ == "__main__":
    data = [
        [
            [-10, -10, 5, 2], 500,
        ],
        [
            [0, 2, -5, 3], 0,
        ],
        [
            [2, 1, 3, -5], 6
        ]
    ]
    for d in data:
        print('input:', d[0], 'output:', largest_product(d[0]))
