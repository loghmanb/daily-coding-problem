'''
Kth Smallest Element In Tree
Asked in: Amazon

https://www.interviewbit.com/problems/kth-smallest-element-in-tree/

Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST
 '''

 # Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @param A : root node of tree
# @param B : integer
# @return an integer
def kthsmallest(A, B):
    stack = [(A, 'l')]
    i_smallest = 0
    while stack:
        n, direction = stack.pop()
        if not n: continue
        
        if direction=='l':
            stack.append((n, 'self'))
            stack.append((n.left, 'l'))
        elif direction=='self':
            i_smallest += 1
            stack.append((n.right, 'l'))
            
        if i_smallest==B:
            return n.val