'''
Palindrome String



Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

# @param A : string
# @return an integer
def isPalindrome(A):
    i,j = 0,len(A)-1
    while i<j:
        if not A[i].isalpha() and not A[i].isnumeric():
                i+=1
        elif not A[j].isalpha() and not A[j].isnumeric():
                j-=1
        elif A[i].lower()!=A[j].lower():
                return 0
        else:
                i+=1
                j-=1
    return 1


if __name__ == "__main__":
    data = [
            ["A man, a plan, a canal: Panama", 1]
    ]

    for d in data:
        print('input', d[0], 'output', isPalindrome(d[0]))