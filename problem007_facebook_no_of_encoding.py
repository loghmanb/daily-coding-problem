'''
This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa',
'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def calc_no_of_ways(w):
    mem = {}
    alphabets = [str(i) for i in range(1, 27)]

    def f(w):
        res = 0
        if w:
            if w in mem:
                res = mem[w]
            else:
                for i in range(1, 27):
                    ch = str(i)
                    if w==ch:
                        res += 1
                    elif w.startswith(ch):
                        res += f(w[len(ch):])
                mem[w] = res
        return res
    
    return f(w)

def calc_no_of_ways_opt(w):
    ways = [0]*(len(w)+1)
    ways[0] = 1
    for i,x in enumerate(w):
        if x>'6' or x=='0' or i>0 and w[i-1]>'2':
            ways[i+1] = ways[i]
        else:
            ways[i+1] = ways[i] + ways[i-1]
    return ways[-1]


if __name__ == '__main__':

    test_list = ['111', '2626']
    
    for s in test_list:
        print( 'string: ', s, ' no of ways: ', calc_no_of_ways(s), ' optimized: ', calc_no_of_ways_opt(s) )