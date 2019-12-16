'''
Identical Binary Trees
Asked in: Amazon

https://www.interviewbit.com/problems/identical-binary-trees/

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 

   1       1
  / \     / \
 2   3   2   3

Output : 
  1 or True


Solution by DFS algorithm
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param A : root node of tree
# @param B : root node of tree
# @return an integer
def isSameTree(A, B):
    if not A and not B: return 1
    elif not A and B or A and not B: return 0
        
    qA = [A]
    qB = [B]
    while qA and qB:
        a = qA.pop()
        b = qB.pop()
        if a.val!=b.val:
            return 0
        if a.right and b.right:
            qA.append(a.right)
            qB.append(b.right)
        elif a.right or b.right:
            return 0
        if a.left and b.left:
            qA.append(a.left)
            qB.append(b.left)
        elif a.left or b.left:
            return 0
    return 1