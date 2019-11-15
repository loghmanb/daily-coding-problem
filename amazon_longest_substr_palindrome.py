'''
Longest Palindarome Substring

https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

Asked by: Amazon

Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana"

Solved by dynamic programming or recursive functions

if S is palindarome so reteurn len of S
else check for S[1:] or S[:-1]

if len of S is equal 1 so return 1 (because of each character is palaindarome)
if len of S is equal 2 and S[0]==S[1] return 2 

'''

def longestPalindromeSubstring(S):
    if not S: return 0
    
    N = len(S)
    table = [[False]*N for _ in range(N)]
    
    start = 0
    maxLen = 1
    
    #Check for single char and double contigues chars
    for i in range(N):
        #Each character is palindarome
        table[i][i] = True
        if i<N-1:
            #Check for two characters
            if table[i][i]==table[i][i+1]:
                start = i
                maxLen = 2

    #Check for 3 and more charachters
    for k in range(3, N+1):
        for i in range(N-k+1):
            #find mirror position of i
            j = i + k - 1
            #str[i:j] is palindarome if str[i+1:j-1] is palindarome and str[i] is equal to str[j]
            if table[i+1][j-1] and S[i]==S[j]:
                table[i][j] = True
                if maxLen<k:
                    maxLen = k
                    start = i
    
    return maxLen

if __name__ == "__main__":
     data = [
             ['aabcdcb', 5]   
     ]

     for d in data:
         print('input', d[0], 'output', longestPalindromeSubstring(d[0]))