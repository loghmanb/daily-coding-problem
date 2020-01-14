'''
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5

'''

from collections import deque

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def bfs(root):
    res = []
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


if __name__ == "__main__":
    data = [
            [
             TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))),
             [1, 2, 3, 4, 5]
            ]
    ]

    for d in data:
        print('input', d[0], 'output', bfs(d[0]))