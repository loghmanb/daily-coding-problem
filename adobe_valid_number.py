'''
Valid Number
Asked in: Adobe

https://www.interviewbit.com/problems/valid-number/

Please Note:
Note: It is intended for some problems to be ambiguous. You should gather all requirements up front before implementing one.

Please think of all the corner cases and clarifications yourself.

Validate if a given string is numeric.

Examples:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Clarify the question using “See Expected Output”

Is 1u ( which may be a representation for unsigned integers valid?
For this problem, no.
Is 0.1e10 valid?
Yes
-01.1e-10?
Yes
Hexadecimal numbers like 0xFF?
Not for the purpose of this problem
3. (. not followed by a digit)?
No
Can exponent have decimal numbers? 3e0.1?
Not for this problem.
Is 1f ( floating point number with f as prefix ) valid?
Not for this problem.
How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
Not for this problem.
How about integers preceded by 00 or 0? like 008?
Yes for this problem
'''

import re

# @param A : string
# @return an integer
def isNumber(A):
    A = A.strip()
    if not A: return 0
    r = "^[-]?[0-9]*([.][0-9]+)?([e][-]?[0-9]+)?$"
    m = re.match(r, A)
    if m and m.start()==0 and m.end()==len(A):
        return 1
    else:
        return 0


if __name__ == "__main__":
    data = [
            ['0', 1],
            [' 0.1', 1],
            ['abc', 0],
            ['1 a', 0],
            ['2e10', 1],
    ]

    for d in data:
        print('input', d[0], 'output', isNumber(d[0]))