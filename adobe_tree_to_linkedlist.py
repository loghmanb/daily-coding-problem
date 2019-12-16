'''
Flatten Binary Tree to Linked List
Asked in: Adobe, Amazon, Microsoft

https://www.interviewbit.com/problems/flatten-binary-tree-to-linked-list/

Given a binary tree, flatten it to a linked list in-place.

Example :
Given


         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val


# @param A : root node of tree
# @return the root node in the tree
def flatten(A):
    if not A or (not A.left and not A.right): return A
    left = flatten(A.left)
    right = flatten(A.right)
    if left:
        A.left = None
        A.right = left
        while left.right:
            left = left.right
        left.right = right         
    return A


if __name__ == "__main__":
    d = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, right=TreeNode(5))))
    flatten(d)