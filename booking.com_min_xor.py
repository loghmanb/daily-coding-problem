'''
Min XOR value
Asked in: Booking.com

https://www.interviewbit.com/problems/min-xor-value/

Problem Setter: mihai.gheorghe Problem Tester: archit.rai
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Input Format:

    First and only argument of input contains an integer array A
Output Format:

    return a single integer denoting minimum xor value
Constraints:

2 <= N <= 100 000  
0 <= A[i] <= 1 000 000 000
For Examples :

Example Input 1:
    A = [0, 2, 5, 7]
Example Output 1:
    2
Explanation:
    0 xor 2 = 2
Example Input 2:
    A = [0, 4, 7, 9]
Example Output 2:
    3
'''

# @param A : list of integers
# @return an integer
def findMinXor(A):
    A = sorted(A)
    min_xor = A[-1]
    for i in range(1, len(A)):
        xor = A[i-1]^A[i]
        if min_xor>xor:
            min_xor = xor
    return min_xor


if __name__ == "__main__":
    data = [
            [[0, 2, 5, 7], 2]
    ]

    for d in data:
        print('input', d[0], 'output', findMinXor(d[0]))