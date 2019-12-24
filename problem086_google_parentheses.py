'''
This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
'''

def noOfWrongParentheses(string):
    ans = 0
    balance = 0
    for ch in string:
        if ch=='(':
            balance += 1
        elif ch==')':
            if balance>0:
                balance -= 1
            else:
                ans += 1
    ans += balance
    return ans


if __name__ == "__main__":
    data = [
            ["()())()", 1],
            [")(", 2]
    ]
    for d in data:
        print('input', d[0], 'output', noOfWrongParentheses(d[0]))