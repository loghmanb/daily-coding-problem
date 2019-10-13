'''
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
'''

def encode_str(s):
    ans = ''
    no = 0
    pre_x = None
    for i,x in enumerate(s):
        if pre_x is None:
            pre_x = x
            no = 1
        elif pre_x==x:
            no += 1
        else:
            ans += '%s%s' % (no, pre_x)
            pre_x = x
            no = 1
        if i==len(s)-1:
            ans += '%s%s' % (no, pre_x)
    return ans

def decode_str(s):
    if not s:
        return s
    
    ans = ''
    no = ''
    for ch in s:
        if ch.isalpha():
            ans += ch * int(no)
            no = ''
        else:
            no += ch
    return ans


if __name__ == '__main__':
    test_list = ['AAAABBBCCDAA',]
    
    for s in test_list:
        print( 'Input: ', s, '', encode_str(s), ' decoded: ', decode_str(encode_str(s)) )