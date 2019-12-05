'''
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

def no_of_ways(N):
    ways = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i==0 or j==0:
                ways[i][j] = 1
            else:
                ways[i][j] = ways[i-1][j] + ways[i][j-1]
    
    return ways[-1][-1]


if __name__=='__main__':
    data = [
            [2, 2],
            [3, 6],
            [5, 70],
        ]
    
    for d in data:
        print('input', d[0], 'output', no_of_ways(d[0]))