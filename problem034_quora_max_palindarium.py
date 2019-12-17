'''
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

Upgrade to premium and get in-depth solutions to every problem, including this one.

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!


Reference: https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
'''

# A Dynamic Programming based program to  
# find minimum number insertions needed  
# to make a str1ing palindrome 
  
  
# A DP function to find minimum number 
# of insertions 
def findMinInsertionsDP(str1, n): 
  
    # Create a table of size n*n. table[i][j] 
    # will store minimum number of insertions  
    # needed to convert str1[i..j] to a palindrome. 
    table = [[0 for i in range(n)]  
                for i in range(n)] 
    l, h, gap = 0, 0, 0
  
    # Fill the table 
    for gap in range(1, n): 
        l = 0
        for h in range(gap, n): 
            if str1[l] == str1[h]: 
                table[l][h] = table[l + 1][h - 1] 
            else: 
                table[l][h] = (min(table[l][h - 1],  
                                   table[l + 1][h]) + 1) 
            l += 1
  
    # Return minimum number of insertions  
    # for str1[0..n-1] 
    return table[0][n - 1]; 