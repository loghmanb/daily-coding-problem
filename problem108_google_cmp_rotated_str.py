'''
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
'''

def is_the_same(s1, s2):
    if len(s1)!=len(s2): return False

    N = len(s1)
    p1, p2, no = 0, 0, 0
    for _ in range(2*N):
        if s1[p1]==s2[p2]:
            p1 = (p1 + 1) % N
            p2 = (p2 + 1) % N
            no += 1
            if no == N:
                return True
        else:
            if no==0:
                p2 += 1
            p1 = no = 0
            
    return False


if __name__ == "__main__":
    data = [
            [['abcabdabe', 'cabdabeab'], True]
    ]
    for d in data:
        print('input', d[0], 'output', is_the_same(*d[0]))