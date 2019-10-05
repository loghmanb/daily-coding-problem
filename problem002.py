'''
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].
Follow-up: what if you can't use division?
'''

def solve(int_list):

    all_product = 1
    for x in int_list:
        all_product *= x

    return list(map(lambda x:int(all_product/x), int_list))


if __name__ == '__main__':
    test_list = [[1, 2, 3, 4, 5],
                 [3, 2, 1]]
    
    for l in test_list:
        print( 'list: ', l, ' output: ', solve(l) )