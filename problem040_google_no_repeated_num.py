'''
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

Solved by https://www.geeksforgeeks.org/find-the-element-that-appears-once/
'''

def getSingle(arr): 
    n = len(arr)
    ones = 0
    twos = 0
      
    for i in range(n): 
        # one & arr[i]" gives the bits that 
        # are there in both 'ones' and new 
        # element from arr[]. We add these 
        # bits to 'twos' using bitwise OR 
        twos = twos | (ones & arr[i]) 
          
        # one & arr[i]" gives the bits that 
        # are there in both 'ones' and new 
        # element from arr[]. We add these 
        # bits to 'twos' using bitwise OR 
        ones = ones ^ arr[i] 
          
        # The common bits are those bits  
        # which appear third time. So these 
        # bits should not be there in both  
        # 'ones' and 'twos'. common_bit_mask 
        # contains all these bits as 0, so 
        # that the bits can be removed from 
        # 'ones' and 'twos' 
        common_bit_mask = ~(ones & twos) 
          
        # Remove common bits (the bits that  
        # appear third time) from 'ones' 
        ones &= common_bit_mask 
          
        # Remove common bits (the bits that 
        # appear third time) from 'twos' 
        twos &= common_bit_mask 
    return ones 


if __name__ == "__main__":
    data = [
            [
             [3, 3, 2, 3],
             2
            ]
    ]
    for d in data:
        print('input', d[0], 'output', getSingle(d[0]))