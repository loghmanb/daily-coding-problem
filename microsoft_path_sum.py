'''
Path Sum
Asked in: Microsoft, Yahoo, Amazon

https://www.interviewbit.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Example :

Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
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
def hasPathSum(A, B):
    s = [(A, 0)]
    while s:
        n, val = s.pop()
        if not n.left and not n.right:
            if val+n.val==B:
                return 1
        else:
            if n.right:
                s.append((n.right, val+n.val))
            if n.left:
                s.append((n.left, val+n.val))
    return 0