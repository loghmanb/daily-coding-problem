'''
Gray Code
Asked in: Microsoft

https://www.interviewbit.com/problems/gray-code/

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.
Return any such sequence.
'''

# @param N : integer
# @return a list of integers
def grayCode(n):
    if n==1:
        return [0, 1]
    arr = grayCode(n-1)
    cnt = 2**(n-1)
    l = len(arr)
    for i in range(l):
        arr.append(cnt+arr[l-i-1])
    return arr

def grayCodeLinear(n):
    ans = []
    if not n: return ans

    ans = [0, 1]
    for no in range(1, n):
        l = len(ans)
        const = 2**no
        for j in range(l):
            ans.append(const+ans[l-j-1])
    return ans
    

if __name__ == "__main__":
    data = [
            [5, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16]]
    ]
    for d in data:
        print('input', d[0], 'output#1', grayCode(d[0]), 'output#2', grayCodeLinear(d[0]))