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


'''
for [a, b, c, d, e]

first step:
    for each item is calculated from previous value to previous position value in main array
    l1 = [1. a, (a)b, (ab)c, (abc)d]
second step;
    repeat what happend before in reverse (from right to left)
    l2 = [b(cde), c(de), d(e), e, 1]
and finally:
    ans = l1[i]*l2[i] for each item
'''
def solve_without_division(int_list):
    n = len(int_list)

    #from left t right
    l1 = [1]*n
    for i in range(1, n):
        l1[i] = l1[i-1] * int_list[i-1]

    #from right to left
    l2 = [1]*n
    for i in range(1, n):
        l2[n-i-1] = l2[n-i] * int_list[n-i]

    ans = [l1[i]*l2[i] for i in range(n)]

    return ans


if __name__ == '__main__':
    test_list = [[1, 2, 3, 4, 5],
                 [3, 2, 1]]
    
    for l in test_list:
        print( 'list: ', l, ' output#1: ', solve(l), 'output#2: ', solve_without_division(l) )