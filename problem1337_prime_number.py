"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""

from collections import defaultdict

def print_prime_numbers(N):
    invalid_nums = defaultdict(set)
    n = 1
    print(n)
    while n<N:
        n = n+1
        if n in invalid_nums:
            for p, coef in invalid_nums[n]:
                invalid = p * (coef + 1)
                invalid_nums[invalid].add((p, coef+1))
            del invalid_nums[n]
        else:
            invalid_nums[n*2] = {(n, 2)}
            print(n)
            
print_prime_numbers(100)



