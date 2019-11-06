'''
N/3 Repeat Number
Asked in: Google

https://www.interviewbit.com/problems/n3-repeat-number/

You’re given a read only array of n integers. 
Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 

Solution:
-------------------------
When we assume that repeated number more than n/3 times, so this number can be visited in normal distribution in every three lenght sub array. in other case it will be visited more than one time in other subarray
'''

# @param A : tuple of integers
# @return an integer
def repeatedNumber(A):
    n = len(A)
    threshold = n//3
    x1, occ1, x2, occ2 = 0, 0, 0, 0

    for x in A:
        if x==x1:
            occ1 += 1
        elif x==x2:
            occ2 += 1
        elif occ1==0:
            x1 = x
            occ1 = 1
        elif occ2==0:
            x2 = x
            occ2 = 1
        else:
            occ1 -= 1
            occ2 -= 1
    occ1, occ2 = 0, 0
    for x in A:
        if x1==x:
            occ1 += 1
        elif x2==x:
            occ2 += 1
    if occ1>threshold:
        return x1
    elif occ2>threshold:
        return x2
    return -1


if __name__=='__main__':
    data = [
            [[1, 2, 3, 1, 1], 1]
           ]
    for d in data:
        print('input', d[0], 'output', repeatedNumber(d[0]))