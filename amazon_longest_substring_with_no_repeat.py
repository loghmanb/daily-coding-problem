'''
Longest Substring Without Repeat
Asked in: Amazon

https://www.interviewbit.com/problems/longest-substring-without-repeat/

Given a string,
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''

# @param A : string
# @return an integer
def lengthOfLongestSubstring(A):
    if not A: return 0
        
    start = 0
    max_len = 0
    chars = {}
    for i,ch in enumerate(A):
        if ch not in chars or chars[ch]<start:
            l = i-start+1
            if max_len<l:
                max_len = l
        else:
            start = chars[ch]+1
        chars[ch] = i
                
    return max_len


if __name__ == "__main__":
    data = [
            ['abcabcbb', 3]
    ]

    for d in data:
        print('input', d[0], lengthOfLongestSubstring(d[0]))