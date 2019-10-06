  
'''
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
'''


def longest_substr(s, k):
    def long_substr(s, k, l=[]):
        if k<0 or not s:
            return ''
        elif k>len(s):
            return None
        
        if s[0] in l:
            return s[0] + long_substr(s[1:], k, l)
        elif k>0:
            return s[0] + long_substr(s[1:], k-1, l+[s[0]])
        else:
            return ''

    longest = ''
    no = 0
    for i in range(len(s)):
        w = long_substr(s[i:], k)
        if w is None:
            continue
        if len(longest)<len(w):
            longest = w
            no = 1
        elif len(longest)==len(w):
            no += 1

    return no


if __name__ == '__main__':
    test_list = [("abcba", 2)]

    for p in test_list:
        print('input: ', p, '\toutput: ', longest_substr(*p))