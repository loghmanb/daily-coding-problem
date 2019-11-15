'''
Count And Say
Asked in: Facebook

https://www.interviewbit.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
'''

# @param A : integer
# @return a strings
def countAndSay(A):
    n = '1'
    for i in range(A-1):
        k = n[0]
        cnt = 1
        val = ''
        for j in range(1, len(n)):
            if n[j]==k:
                cnt += 1
            else:
                val += '%s%s' % (cnt, k)
                k = n[j]
                cnt = 1
        n = '%s%s%s' % (val, cnt, k)
    return n


if __name__ == "__main__":
    data = [
            [5, '111221']
    ]
    for d in data:
        print('input', d[0], 'output', countAndSay(d[0]))