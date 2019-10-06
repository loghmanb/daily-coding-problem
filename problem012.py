'''
This problem was asked by Amazon.
There exists a staircase with N steps, and you can climb up either 1 or 2 steps
at a time. Given N, write a function that returns the number of unique ways you
can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb
any number from a set of positive integers X? For example, if X = {1, 3, 5}, you
could climb 1, 3, or 5 steps at a time.
-----------------------------------------
Solution:
This problem is similar to Coin Change problems!
In other words, how many ways are there to make number N with coins (c1, c2, ...),
but the order of combination is important!

for instance: 
In above example
    (2, 1, 1) or (1, 2, 1) or (1, 1, 2) is the same in coin change problem 
but here, the order of occurance is important!
'''


def no_of_way_optimized(n, steps):
    ways = [1] + [0] * n

    for i in range(1, n+1):
        for s in steps:
            if i>=s:
                ways[i] += ways[i-s]
    
    return ways[-1]


if __name__ == '__main__':

    test_list = [(4, [1, 2]),
                 (4, [1,3, 5]),
                 (10, [2,5,3,6])]
    
    for p in test_list:
        print( 'input: ', p, ' output: ', no_of_way_optimized(*p))
