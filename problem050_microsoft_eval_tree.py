'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5)
'''

import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def eval(btree):
    if btree.val in ('+', '−', '*', '/'):
        return ops[btree.val](eval(btree.left), eval(btree.right))
    else:
        return int(btree.val)


if __name__ == "__main__":
    btree = TreeNode('*', 
                     TreeNode('+', TreeNode('3'), TreeNode('2')),
                     TreeNode('+', TreeNode('4'), TreeNode('5')))
    print('output', eval(btree))