'''
Minimum Characters required to make a String Palindromic
Asked in: Amazon

https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/

Problem Setter: glowing_glare Problem Tester: RAMBO_tejasv
Given an string A. The only operation allowed is to insert characters in the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.

Input Format

The only argument given is string A.
Output Format

Return the minimum characters that are needed to be inserted to make the string a palindrome string.
For Example

Input 1:
    A = "ABC"
Output 1:
    2
    Explanation 1:
        Insert 'B' at beginning, string becomes: "BABC".
        Insert 'C' at beginning, string becomes: "CBABC".

Input 2:
    A = "AACECAAAA"
Output 2:
    2
    Explanation 2:
        Insert 'A' at beginning, string becomes: "AAACECAAAA".
        Insert 'A' at beginning, string becomes: "AAAACECAAAA".

Solved by interviewbit
'''

# @param A : string
# @return an integer
def solve(A):
    # A palindromic string is equal to its reverse
    reverse = A[::-1]
    if reverse == A:
        return 0
            
    # Every string can be made a palindrome by prepending
    # (or appending) the reverse, and the outermost letter
    # can be ignored. An initial part of the reverse might
    # suffice if there are duplicate letters, so just count
    # how much of the reverse we need:
    for i in range(1, len(reverse)):
        if reverse[:i] + A == reverse + A[-i:]:
            break
    return i

if __name__ == "__main__":
    data = [
            ['AAACECAAAA', 1],
            ['google', 2],
            ['ABC', 2],
            ['ABBABBA', 0],
    ]

    for d in data:
        print('input', d[0], 'output', solve(d[0]))