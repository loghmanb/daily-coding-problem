'''
Inorder Traversal of Cartesian Tree
Asked in: Amazon

https://www.interviewbit.com/problems/inorder-traversal-of-cartesian-tree/

Given an inorder traversal of a cartesian tree, construct the tree.

 Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree. 
 Note: You may assume that duplicates do not exist in the tree. 
Example :

Input : [1 2 3]

Return :   
          3
         /
        2
       /
      1

Solved by interviewbit.com
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param A : list of integers
# @return the root node in the tree
def buildTree(A):
    root = None
    for i in range(len(A)):
        n = TreeNode(A[i])
        if root is None:
            root = n
        else:
            tmp = root
            while tmp.right is None or tmp.right.val<A[i]:
                tmp = tmp.right
            x = tmp.right
            tmp.right = n
            n.left = x
    return root