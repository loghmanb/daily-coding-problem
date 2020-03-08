'''
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
'''
import unittest

def calc_max_profit(arr, k, pre_profit=0):
    if k<=0: return pre_profit
    if len(arr)<2: return None

    profits = []
    buy = sell = arr[0]
    for i in range(1, len(arr)):
        if arr[i]>=sell:
            sell = arr[i]
            profit = calc_max_profit(arr[i+1:], k-1, pre_profit+sell-buy)
            if profit is not None:
                profits.append(profit)
    profit = calc_max_profit(arr[1:], k, pre_profit)
    if profit is not None:
        profits.append(profit)

    return profits and max(profits) or None


class CalcMaxProfit(unittest.TestCase):

    def test_check_max_profit(self):
        max_profit = calc_max_profit([5, 2, 4, 0, 1], 2)
        self.assertEqual(3, max_profit)

if __name__ == "__main__":
    
    unittest.main()