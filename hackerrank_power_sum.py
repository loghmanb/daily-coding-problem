'''
https://www.hackerrank.com/challenges/the-power-sum/problem

Find the number of ways that a given integer, X, can be expressed as the sum of the Nth powers of unique, natural numbers.

For example, if X=13 and N=2, we have to find all combinations of unique squares adding up to 13. The only solution is 2^2 + 3^2.
'''

def powerSum(X, N, i=1):
    iN = pow(i, N)
    if iN<X:
        ans = powerSum(X-iN, N, i+1)
        ans += powerSum(X, N, i+1)
        return ans
    elif iN==X:
        return 1
    else:
        return 0

if __name__ == '__main__':
    data = [
            [13, 2],
            [100, 2],
           ]
    
    for l in data:
        print('the num of ways for ', l[0], ' as the sum of ', l[1], 'th of unique, natural numbers is ', powerSum(*l))