'''
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.


This code is contributed by Rituraj Jain 

https://www.geeksforgeeks.org/n-th-number-whose-sum-of-digits-is-ten/

'''

# Python3 program to find the n-th number  
# with the sum of digits as 10.  
import math 
  
def findNth(n):  
  
    nthElement = 19 + (n - 1) * 9
    outliersCount = int(math.log10(nthElement)) - 1
  
    # find the nth perfect number  
    nthElement += 9 * outliersCount  
    return nthElement  
  
# Driver Code  
if __name__ == "__main__":  
  
    print(findNth(5))  