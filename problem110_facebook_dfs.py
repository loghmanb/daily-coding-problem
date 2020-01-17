'''
This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def dfs(root):
    result = []
    stack = [(root, [])]
    while stack:
        node, nodes_chain = stack.pop()
        if node.left is None and node.right is None:
            result.append(nodes_chain+[node.val])
        else:
            if node.right:
                stack.append((node.right, nodes_chain+[node.val]))
            if node.left:
                stack.append((node.left, nodes_chain+[node.val]))
    return result


if __name__ == "__main__":
    data = [
            [
             TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))),
             [[1, 2], [1, 3, 4], [1, 3, 5]]
            ]
        ]
    for d in data:
        print('input', d[0], 'output', dfs(d[0]))