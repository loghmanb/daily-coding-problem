'''
Sum Root to Leaf Numbers
Asked in: Google, Microsoft

https://www.interviewbit.com/problems/sum-root-to-leaf-numbers/

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param A : root node of tree
# @return an integer
def sumNumbers(A):
    if not A: return 0
        
    ans = 0
    stack = [(A, 0)]
    while stack:
        n, v = stack.pop()
        v = v*10+n.val
        if not n.left and not n.right:
            ans += v%1003
        if n.right:
            stack.append((n.right, v))
        if n.left:
            stack.append((n.left, v))
    return ans%1003