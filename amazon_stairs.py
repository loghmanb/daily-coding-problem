'''
Stairs
Asked in: Morgan Stanley, Amazon, Intel

https://www.interviewbit.com/problems/stairs/

You are climbing a stair case and it takes A steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Input Format:

The first and the only argument contains an integer A, the number of steps.
Output Format:

Return an integer, representing the number of ways to reach the top.
Constrains:

1 <= A <= 36
Example :

Input 1:

A = 2 Output 1:

2 Explanation 1:

[1, 1], [2] Input 2:

A = 3 Output 2:

3 Explanation 2: 

[1 1 1], [1 2], [2 1]
'''

# @param N : integer
# @return an integer
def climbStairs(N):
    if not N: return 1
        
    steps = [0] * (N+1)
    steps[0] = steps[1] = 1
    for i in range(2, N+1):
        steps[i] = steps[i-1] + steps[i-2]
    return steps[-1]


if __name__ == "__main__":
    data = [
            [4, 5]
    ]
    for d in data:
        print('input', d[0], 'output', climbStairs(d[0]))