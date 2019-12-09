'''
Evaluate Expression
Asked in: Yahoo, Google, Facebook

https://www.interviewbit.com/problems/evaluate-expression/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.



Input Format

The only argument given is character array A.
Output Format

Return the value of arithmetic expression formed using reverse Polish Notation.
For Example

Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9
    
Input 2:
    A = ["4", "13", "5", "/", "+"]
Output 2:
    6
Explaination 2:
    +: ()+()
    /: ()+(() / ())
    5: ()+(() / (5))
    1: ()+((13) / (5))
    4: (4)+((13) / (5))
    (4)+((13) / (5)) = 6
'''

# @param A : list of strings
# @return an integer
def evalRPN(A):
    if not A: return 0
        
    x = A.pop()
    if x in ('+', '-', '*', '/'):
        b = evalRPN(A)
        a = evalRPN(A)
        if x=='+':
            return a+b
        elif x=='-':
            return a-b
        elif x=='*':
            return a*b
        else:
            return a/b
    else:
        return int(x)


if __name__ == "__main__":
    data = [
            [["2", "1", "+", "3", "*"], 9]
    ]

    for d in data:
        print('input', d[0], 'output', evalRPN(d[0][:]))