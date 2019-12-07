'''
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''

def findInMatrix(mat, s):
    N = len(mat)
    M = len(mat[0])

    founds = []
    for i in range(N):
        for j in range(M):
            for case in founds:
                if case['dir']=='row':
                    if case['row']==i and \
                            case['col']==j-1 and \
                            s[case['index']+1]==mat[i][j]:
                        case['col'] = j
                        case['index'] += 1
                    else:
                        founds.remove(case)
                else:
                    if case['col']==j:
                        if case['row']==i-1 and \
                                s[case['index']+1]==mat[i][j]:
                            case['row'] = i
                            case['index'] +=1
                        else:
                            founds.remove(case)
                if case['index']>=len(s)-1:
                    return True
            if mat[i][j]==s[0]:
                if M-j>=len(s):
                    founds.append({'dir':'row', 'row':i, 'col':j, 'index':0})
                if N-i>=len(s):
                    founds.append({'dir':'col', 'row':i, 'col':j, 'index':0})
                if len(s)==1:
                    return True
    return False


if __name__ == "__main__":
    data = [
            [
             [
                [['F', 'A', 'C', 'I'],
                ['O', 'B', 'Q', 'P'],
                ['A', 'N', 'O', 'B'],
                ['M', 'A', 'S', 'S']],
                'FOAM'
             ], 
             True
            ]
    ]

    for d in data:
        print('input', d[0], 'output', findInMatrix(*d[0]))

