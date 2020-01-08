  
'''
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".


'''

# It has been already solved in https://github.com/loghmanb/daily-coding-problem/blob/master/amazon_longest_substring_with_no_repeat.py with better approach

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

def longest_substr_optimized(s, k):
    letters = {}
    start = 0
    N = len(s)
    max_len = 0
    max_str = ''
    for i,ch in enumerate(s):
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] += 1
        l = len(letters.keys())
        if l==k:
            if max_len<(i-start+1):
                max_str = s[start:i+1]
                max_len = i-start+1
        elif l>k:
            while len(letters.keys())>k:
                letters[s[start]] -= 1
                if letters[s[start]]==0:
                    del letters[s[start]]
                start += 1
    return max_str


if __name__ == '__main__':
    test_list = [("abcba", 2)]

    for p in test_list:
        print('input: ', p, '\toutput: ', longest_substr(*p), '\toutput optimized', longest_substr_optimized(*p))