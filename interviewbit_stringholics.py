'''
Stringoholics

https://www.interviewbit.com/problems/stringoholics/

You are given an array A consisting of strings made up of the letters ‘a’ and ‘b’ only.
Each string goes through a number of operations, where:

1.	At time 1, you circularly rotate each string by 1 letter.
2.	At time 2, you circularly rotate the new rotated strings by 2 letters.
3.	At time 3, you circularly rotate the new rotated strings by 3 letters.
4.	At time i, you circularly rotate the new rotated strings by i % length(string) letters.

Eg: String is "abaa"

1.	At time 1, string is "baaa", as 1 letter is circularly rotated to the back
2.	At time 2, string is "aaba", as 2 letters of the string "baaa" is circularly rotated to the back
3.	At time 3, string is "aaab", as 3 letters of the string "aaba" is circularly rotated to the back
4.	At time 4, string is again "aaab", as 4 letters of the string "aaab" is circularly rotated to the back
5.	At time 5, string is "aaba", as 1 letters of the string "aaab" is circularly rotated to the back
After some units of time, a string becomes equal to it’s original self.
Once a string becomes equal to itself, it’s letters start to rotate from the first letter again (process resets). So, if a string takes t time to get back to the original, at time t+1 one letter will be rotated and the string will be it’s original self at 2t time.
You have to find the minimum time, where maximum number of strings are equal to their original self.
As this time can be very large, give the answer modulo 10**9+7.

Note: Your solution will run on multiple test cases so do clear global variables after using them.

Input:

A: Array of strings.
Output:

Minimum time, where maximum number of strings are equal to their original self.
Constraints:

1 <= size(A) <= 10^5
1 <= size of each string in A <= 10^5
Each string consists of only characters 'a' and 'b'
Summation of length of all strings <= 10^7
Example:

Input

A: [a, ababa, aba]
Output

4

String 'a' is it's original self at time 1, 2, 3 and 4.
String 'ababa' is it's original self only at time 4. (ababa => babaa => baaba => babaa => ababa)
String 'aba' is it's original self at time 2 and 4. (aba => baa => aba)

Hence, 3 strings are their original self at time 4.

Solved by Interviewbit!

Access Hint
With respect to a single string, the total number of bits rotated after N operations is 1+2+3+….+N which is (N*(N+1))/2.
We get back the original string only when the total number of rotated bits is a multiple of the length of the string S(LEN).

This can be done in O(N) time for each string (Summation of length of all strings is <= 1e6), by finding all (N(N+1))/2 where N starts from 1 and goes upto (2LEN-1).

But there is a catch, this wont always give you the minimum number of operations.
Its possible that during rotation, you can get the original string before the number of bits rotated is a multiple of LEN.

Example: S=> 100100
Here, in 2 operations, we get the original string back.
This takes place because the string is made up of recurring substrings.

Assume string A to be 100
S => AA
Hence, over here our length S of string is the length of recurring substring A, so N*(N+1)/2 should be a multiple of length of A.

Length of recurring substring can easily be found out using KMP algorithm in O(N) time complexity for each string.

Find the minimum number of operations for each string, and take the LCM of all these values to get the answer.
Handling of overflow for LCM should be handled by breaking the number down into factors, and then taking LCM (Not needed for languages that don’t have integer limit).

Hence total time complexity is O(N).

'''

def computeLPSArray(pat, M):
    lps=[0]*M
    len = 0
    lps[0] # lps[0] is always 0
    i = 1
    while i < M:
        if pat[i]==pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
    len=lps[M-1]
    if(M%(M-len)==0):
        return M-len
    else:
        return M
            
def gcd(A,B):
    if(B>A):
        A,B = B,A
    if(B==0):
        return A
    return gcd(B,A%B)
            
# @param A : list of strings
# @return an integer
def solve(A):
    ans=1
    for k in A:
        res = computeLPSArray(k, len(k))
        for i in range(1,1000000000):
            if(((i*(i+1))//2) % len(k)==0):
                ans=((ans*i)//gcd(ans,i))
                break
    return (ans%1000000007)

if __name__ == "__main__":
    data = [
            [
                ['a', 'ababa', 'aba'],
                4
            ]
    ]
    for d in data:
        print('input', d[0], 'output', solve(d[0]))