'''
Booking.com Interview Question for Software Engineer / Developers

https://www.careercup.com/question?id=5739532692488192

Given number N, Find the least number of perfect square number sum needed to get N.

Example : 
n=5 (4+1) i.e. 2
n=7 (4+1+1+1) i.e. 4
n=12 (4+4+4) i.e 3
n=20 (16+4) i.e. 2
'''

import math
import sys


def find_no_of_perfect_square(n):
    if n<0:
        return sys.maxsize
    if n<4:
        return n
    elif n==4:
        return 1
    
    root = int(math.sqrt(n))
    if root>=2:
        return min(
            1+find_no_of_perfect_square(n-pow(root, 2)),
            n//pow(root-1,2) + find_no_of_perfect_square(n%pow(root-1,2))
        )
    else:
        return n


if __name__=='__main__':
    data = [
            [5, 2],
            [7, 4],
            [12, 3],
            [20, 2],
            ]
    for d in data:
        print('the least no of perfect square for', d[0], 'is', find_no_of_perfect_square(d[0]), 'expected', d[1])