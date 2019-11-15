'''
https://www.hackerrank.com/challenges/sam-and-substrings/problem

Samantha and Sam are playing a numbers game. Given a number as a string, no leading zeros, 
determine the sum of all integer values of substrings of the string. 
For example, if the string is 16 , the substrings are 1, 6 and 16. Their sum is 23.

Given an integer as a string, sum all of its substrings cast as integers. As the number may become large, 
return the value modulo 10^9+7.

Function Description

Write the substrings function in which it should return the sum of the integer values of all substrings in a string representation of a number, modulo 10^9+7.

substrings has the following parameter(s):

n: the string representation of an integer
Input Format

A single line containing an integer as a string without leading zeros.

Constraints

Output Format

A single line which is sum of the substrings, 

Sample Input 0

16
Sample Output 0

23
Explanation 0

The substring of number 16 are 16, 1 and 6 which sums to 23.

Sample Input 1

123
Sample Output 1

164
Explanation 1

The sub-strings of 123 are 1, 2, 3, 12, 23, 123 which sums to 164.


Solution:
-------------------
N = 5234

5 + 52 + 523 + 5234 + 2 + 23 + 234 + 3 + 34 + 4

grouping by ends with this number:

5    | 2 + 52           | 3 + 23 + 523     | 4 + 34 + 234 + 5234 = 4*4 + 10 * (3 + 23 + 523)

N[0] | 2*N[1] + 10*G[0] | 3*N[2] + 10*G[1] | 4*N[3] + 10*G[2]

G[0] | G[1]             | G[2]             | G[3]

'''

def solution(N):
    N = str(N)
    l = len(N)
    G = [0]*l

    G[0] = int(N[0])
    ans = G[0]
    for i in range(l-1):
        G[i+1] = (2+i)*int(N[i+1]) + (10*G[i]) % 1000000007
        ans = (ans + G[i+1]) % 1000000007
    
    return ans % 1000000007

if __name__ == "__main__":
    data = [
            [123, 164]   
    ]

    for d in data:
        print('input', d[0], solution(d[0]))