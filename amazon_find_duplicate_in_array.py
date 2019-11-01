'''
Find Duplicate in Array
Asked in: Amazon, VMWare, Riverbed

https://www.interviewbit.com/problems/find-duplicate-in-array/

Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
'''

# @param A : tuple of integers
# @return an integer
def repeatedNumber(A):
    pos = {}
    for x in A:
        if x in pos:
            return x
        pos[x] = True
    return -1


if __name__ == "__main__":
    data = [
            [[3, 4, 1, 4, 1], 1]
        ]

    for d in data:
        print('input', d[0], 'output', repeatedNumber(d[0]))