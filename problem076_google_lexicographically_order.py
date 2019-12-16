'''
This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the columns to order it.
'''

def check(s1, s2, removed_cols):
    for i in removed_cols:
        s1 = s1[:i] + s1[i+1:]
        s2 = s2[:i] + s2[i+1:]
    return bool(s1<=s2)

def solve(arr):
    if not arr or len(arr)==1: 
        return 0

    removed_cols = []
    N = len(arr)
    M = len(arr[0])
    for j in range(M):
        for i in range(1, N):
            if arr[i-1][j]>arr[i][j]:
                removed_cols.append(j)
                break
            elif j>1 and not check(arr[i-1][:j-1], arr[i][:j-1], removed_cols):
                removed_cols.append(j)
                break
    return len(removed_cols)


if __name__ == "__main__":
    data = [
            [
                ['cba', 'daf', 'ghi'], 1
            ],
            [
                ['abcdef'], 1
            ],
            [
                ['zyx', 'wvu', 'tsr'], 3
            ]
    ]
    for d in data:
        print('input', d[0], 'output', solve(d[0]))