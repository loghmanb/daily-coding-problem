'''
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '%s [%s , %s]' % (self.val, self.left or '', self.right or '')

def create_pre_order(arr):
    N = len(arr)
    if not N: 
        return None
    root = TreeNode(arr[0])
    N = (N-1)//2+1
    root.left = create_pre_order(arr[1:N])
    root.right = create_pre_order(arr[N:])
    return root


if __name__ == "__main__":
    data = [
            [
                ['a', 'b', 'd', 'e', 'c', 'f', 'g']
            ]
    ]
    for d in data:
        create_pre_order(d[0])
