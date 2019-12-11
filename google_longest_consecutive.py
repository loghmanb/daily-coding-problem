'''
Longest Consecutive Sequence
Asked in: Amazon, Google

https://www.interviewbit.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Solution by interviewbit
'''

# @param A : tuple of integers
# @return an integer
def longestConsecutive(A):
    consecutive_dict = {}
    for x in A:
        if x-1 in consecutive_dict:
            consecutive_dict[x] = consecutive_dict[x-1] + 1
        else:
            consecutive_dict[x] = 1
        while True:
            if x+1 in consecutive_dict:
                consecutive_dict[x+1] = consecutive_dict[x]+1
                x += 1
            else:
                break
    return max(consecutive_dict.values())


if __name__ == "__main__":
    data = [
            [[100, 4, 200, 1, 3, 2], 4]
    ]

    for d in data:
        print('input', d[0], 'output', longestConsecutive(d[0]))