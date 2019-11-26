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
'''

# @param A : string
# @return an integer
def solve(A):
    N = len(A)
    ans = 0
    start = 0
    for i in range(N):
        if start>=N-i-1:
            break
        if A[N-i-1]!=A[start]:
            if start>0:
                if A[N-i-1]==A[0]:
                    start = 1
                    ans = i
                    continue
            start = 0
            ans = i+1
        else:
            start += 1
    return ans


if __name__ == "__main__":
    data = [
            ['ABC', 2],
            ['ABBABBA', 0],
    ]

    for d in data:
        print('input', d[0], 'output', solve(d[0]))