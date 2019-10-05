  
'''
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.
You can modify the input array in-place.
-----------
You can find some useful discussion for solving this problem from https://github.com/Jedshady/daily-coding-problem/blob/master/Problem%201-30/problem_4.py

But here, you will find a optimized Complexity and Memory solution!
RangedBinaryTree!
'''

class Node:
    left = None
    right = None
    left_val = None
    right_val = None

    def __init__(self, val=None):
        self.left_val = val
        self.right_val = val
    
    def add(self, val):
        if val<1: return
        elif self.left_val is None or self.right_val is None:
            self.left_val = self.right_val = val
            return

        if val==self.left_val-1:
            self.left_val = val
        elif val==self.right_val+1:
            self.right_val = val
        elif val<self.left_val:
            if self.left:
                self.left.add(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = Node(val)
        if self.left and self.left.right_val+1==self.left_val:
            self.left_val = self.left.left_val
            self.left = self.left.left
        if self.right and self.right.left_val-1==self.right_val:
            self.right_val = self.right.right_val
            self.right = self.right.right

    def find_min_positive(self):
        node = self
        while node.left:
            node = node.left
        return node.right_val+1

    def __str__(self):
        return '[%s~%s] (%s, %s)' % ( self.left_val, self.right_val, self.left, self.right)


if __name__ == '__main__':

    test_list = [[3, 4, -1, 1]]
    
    for l in test_list:
        n = Node()
        for i in l:
            n.add(i)
        print( 'input: ', l, ' output:', n.find_min_positive() )

