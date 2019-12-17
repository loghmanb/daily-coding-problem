'''
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
'''

def deapestChild(root):
    if not root: return
    deapest = None
    deapest_len = 0
    stack = [(root, 1)]
    while stack:
        n, l = stack.pop()
        if not n.right:
            stack.append((n.right, l+1))
        if not n.left:
            stack.append((n.left, l+1))
        if not n.left and n.right and deapest_len>l:
            deapest, deapest_len = n, l
    return deapest