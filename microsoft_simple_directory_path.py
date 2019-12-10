'''
Simplify Directory Path
Asked in:  
Microsoft
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

Absolute path always begin with ’/’ ( root directory ).

Path will not have whitespace characters.



Input Format

The only argument given is string A.
Output Format

Return a string denoting the simplified absolue path for a file (Unix-style).
For Example

Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"
'''

# @param A : string
# @return a strings
def simplifyPath(A):
    A = A.split('/')
    path = []
    for x in A:
        if not x or x=='.':
            pass
        elif x=='..':
            if path:
                path.pop()
        else:
            path.append(x)
    path = '/' + '/'.join(path)
    return path


if __name__ == "__main__":
    data = [
            ['/home/', '/home'],
            ['/a/./b/../../c/', '/c']
    ]

    for d in data:
        print('input', d[0], 'output', simplifyPath(d[0]))