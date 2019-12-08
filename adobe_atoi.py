'''
Atoi

Asked in: Adobe, Nvidia, Agilent systems, Bloomberg, Amazon, Apple, Microsoft, Groupon

https://www.interviewbit.com/problems/atoi/

Please Note:
There are certain questions where the interviewer would intentionally frame the question vague.
The expectation is that you will ask the correct set of clarifications or state your assumptions before you jump into coding.

Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

 Questions: Q1. Does string contain whitespace characters before the number?
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise. 
Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''

INT_MAX = 2147483647
INT_MIN = -2147483648

# @param A : string
# @return an integer
def atoi(A):
    ans = ''
    is_negative = False
    is_started = False
    for i,x in enumerate(A):
        if not is_started:
            if x==' ':
                pass
            elif x=='+':
                is_started = True
            elif x=='-':
                is_started = True
                is_negative = True
            elif x.isdigit():
                ans += x
                is_started = True
            else:
                return 0
        elif x.isdigit():
                ans += x
        else:
            break
    ans = int(ans or '0')
    if is_negative:
        ans = -ans
    if ans>INT_MAX:
        ans = INT_MAX
    elif ans<INT_MIN:
        ans = INT_MIN
    return ans


if __name__ == "__main__":
    data = [
            ['9 2704', 9]
    ]
    for d in data:
        print('input', d[0], 'output', atoi(d[0]))