'''
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

def power_set(arr):
    if not len(arr): 
        return arr
    elif len(arr)==1:
        return [[]] + [[arr[0]]]

    sub_power_set = power_set(arr[1:])
    res = sub_power_set[:]
    for item in sub_power_set:
        res.append([arr[0]]+item)
    return res

if __name__ == "__main__":
    data = [
            [
                [1, 2, 3]
            ]
    ]
    for d in data:
        print('input', d[0], 'output', power_set(d[0]))