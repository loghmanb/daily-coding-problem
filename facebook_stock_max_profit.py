'''
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

'''

def maxProfit(arr):
    n = len(arr)
    buy = arr[0]
    max_profit = 0
    for i in range(1, n):
        if arr[i]>buy:
            if max_profit<(arr[i]-buy):
                max_profit = arr[i]-buy
        elif buy>arr[i]:
            buy = arr[i]
    return max_profit

if __name__ == "__main__":
    data = [
            [[9, 11, 8, 5, 7, 10], 5]   
    ]
    for d in data:
        print('input', d[0], maxProfit(d[0]))