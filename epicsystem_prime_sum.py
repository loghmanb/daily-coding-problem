'''
Prime Sum
Asked in: Epic systems

https://www.interviewbit.com/problems/prime-sum/

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 

If a < c OR a==c AND b < d. 

Solved by interviewbit.com
'''

# @param A : integer
# @return a list of integers
def primesum(self, A):
    prime_no = [True]*(A+1)
    prime_no[0], prime_no[1] = False, False
        
    for i in range(2, A+1):
        if prime_no[i]:
            for k in range(i*2, A+1, i):
                prime_no[k] = False
    
    for i in range(A):
        if prime_no[i] and prime_no[A-i]:
            return [i, A-i]
        
    return []


if __name__ == "__main__":
    data = [
            [4, [2, 2]]
    ]
    for d in data:
        print('input', d[0], 'output', primesum(d[0]))