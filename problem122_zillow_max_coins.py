'''
This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. 
Assuming we start at matrix[0][0], and can only move right or down, 
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
'''

import unittest

def max_coin(arr):
    if not arr: return 0

    N = len(arr)
    M = len(arr[0])
    coins = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i==0 or j==0:
                coins[i][j] = arr[i][j]
            else:
                coins[i][j] = arr[i][j] + max(coins[i-1][j], coins[i][j-1])
    return coins[-1][-1]


class MaxCoinsTest(unittest.TestCase):

    def test_max_coin_1(self):
        result = max_coin([
                            [0, 3, 1, 1,],
                            [2, 0, 0, 4,],
                            [1, 5, 3, 1,],
                                         ])
        expected = 12
        self.assertEqual(result, expected)


if __name__ == "__main__":
    
    unittest.main()