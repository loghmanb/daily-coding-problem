'''
Colorful Number

Asked in: Epic systems

https://www.interviewbit.com/problems/colorful-number/

Solution by https://interviewbit.com

For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1
'''

from functools import reduce

def colorful_no(A):
    products = set()
    A = str(A)
    N = len(A)

    for i in range(N):
        for j in range(i+1, N+1):
            n = reduce(lambda x,y:x*y, list(map(int, A[i:j])))
            if n in products:
                return 0
            else:
                products.add(n)
    return 1

if __name__ == "__main__":
    data = [
            [23, 1]
    ]

    for d in data:
        print('input', d[0], 'output', colorful_no(d[0]))