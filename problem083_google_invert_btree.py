'''
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
    
    def __str__(self):
        if not self.left and not self.right:
            return str(self.val)
        return '%s[%s , %s]' % (self.val, self.left, self.right)


def invertBTree(node):
    stack = [node]
    while stack:
        n = stack.pop()
        if n:
            stack.append(n.left)
            stack.append(n.right)
            n.left, n.right = n.right, n.left
    return node


if __name__ == "__main__":
    root = TreeNode('a', TreeNode('b', TreeNode('d'), TreeNode('e')), TreeNode('c', TreeNode('f')))
    print('input', root)
    print('output', invertBTree(root))
