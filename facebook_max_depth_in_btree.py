'''
Max Depth of Binary Tree
Asked in: Goldman Sachs, Facebook, Bloomberg, Microsoft

https://www.interviewbit.com/problems/max-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

 NOTE : The path has to end on a leaf node. 
Example :

         1
        /
       2
max depth = 2.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param A : root node of tree
# @return an integer
def maxDepth(A):
    if not A: return 0
        
    max_depth = 0
    stack = [(A, 1)]
    while stack:
        n, d = stack.pop()
        if not n.left and not n.right:
            if max_depth<d:
                max_depth = d
        if n.right:
            stack.append((n.right, d+1))
        if n.left:
            stack.append((n.left, d+1))
    return max_depth