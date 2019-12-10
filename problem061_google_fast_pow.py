'''
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''

def fast_pow(no, power):
    ans = no
    rem = 1
    while power>1:
        if power%2==1:
            rem *= ans
        power //= 2
        if power>0:
            ans *= ans
    ans *= rem
    return ans


if __name__ == "__main__":
    data = [
            [[2, 10], 1024],
            [[3, 13], 1594323]
    ]

    for d in data:
        print('input', d[0], 'output', fast_pow(*d[0]), 'expected', d[1])
