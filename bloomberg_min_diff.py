'''
Bloomberg LP Interview Question for Software Engineer Interns

Find the two elements that have the smallest difference in a given array.

'''

def find_min_diff(arr):
    arr = sorted(arr)
    min_diff = None
    for i in range(1, len(arr)):
        diff = arr[i]-arr[i-1]
        if min_diff is None or min_diff>diff:
            min_diff = diff
    return min_diff


if __name__=='__main__':
    data = [
            [[100, 20, 52, 18, -4], 2]
           ]

    print('Find minimum difference between items in array')
    for d in data:
        print('array is', d[0], 'result', find_min_diff(d[0]), 'expected', d[1])