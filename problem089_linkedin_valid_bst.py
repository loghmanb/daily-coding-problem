'''
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if not self.left and not self.right: return str(self.val)
        return "%s [%s, %s]" % (self.val, self.left, self.right)


def is_valid_bst(node):
    stack = [(node, float('-inf'), float('inf'))]
    while stack:
        node, min_val, max_val = stack.pop()
        if node.left:
            if node.left.val>node.val \
                    or node.left.val<min_val:
                return False
            stack.append((node.left, min_val, node.val))
        if node.right:
            if node.right.val<node.val \
                    or node.right.val>max_val:
                return False
            stack.append((node.right, node.val, max_val))
    return True

if __name__ == "__main__":
    data = [
            [TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3))), False],
            [TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(9))), True],
    ]

    for d in data:
        print('input', d[0], 'output', is_valid_bst(d[0]))