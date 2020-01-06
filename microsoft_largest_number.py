'''
https://www.interviewbit.com/problems/largest-number/

Largest Number

Asked in: Amazon, Goldman Sachs, Microsoft

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

'''

from functools import cmp_to_key

# @param A : tuple of integers
# @return a strings
def largestNumber(A):
    def cmp_numbers(a, b):
        if len(a)==len(b):
            return 1 if a<b else -1
        m = min(len(a), len(b))
        if a[:m]==b[:m]:
            if len(a)<len(b):
                return cmp_numbers(a, b[m:])
            else:
                return cmp_numbers(a[m:], b)
        else:
            return 1 if a[:m]<b[:m] else -1
                
    A = [str(x) for x in A]
    A = sorted(A, key=cmp_to_key(cmp_numbers))
    ans = ''.join(A)
    if len(ans)>1 and ans[0]=='0':
        ans = '0'
    return ans


if __name__ == "__main__":
    data = [
            [[3, 30, 34, 5, 9], 9534330]
    ]

    for d in data:
        print('input', d[0], 'output', largestNumber(d[0]))