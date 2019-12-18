'''
Min Depth of Binary Tree
Asked in: Facebook, Amazon

https://www.interviewbit.com/problems/min-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

 NOTE : The path has to end on a leaf node. 
Example :

         1
        /
       2
min depth = 2.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def minDepth(A):
    if not A: return 0
        
    min_depth = None
    stack = [(A, 1)]
    while stack:
        n, d = stack.pop()
        if not n.left and not n.right:
            if min_depth is None or min_depth>d:
                min_depth = d
        if n.right:
            stack.append((n.right, d+1))
        if n.left:
            stack.append((n.left, d+1))
    return min_depth 
