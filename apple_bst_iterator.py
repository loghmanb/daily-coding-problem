'''
BST Iterator
Asked in: Apple, Amazon, Facebook

https://www.interviewbit.com/problems/bst-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

 Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
Try to optimize the additional space complexity apart from the amortized time complexity. 
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        if not self.left and not self.right: 
            return str(self.val)
        return '%s (%s, %s)' % (self.val, self.left, self.right)


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        if not root: 
            self.stack = []
            return
        self.stack = [(root, -1)]
        while True:
            n, act = self.stack.pop()
            self.stack.append((n, 0))
            if not n.left:
                break
            self.stack.append((n.left, -1))

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return bool(self.stack)

    # @return an integer, the next smallest number
    def next(self):
        if not self.stack: 
            return
        n, act = self.stack.pop()
        if act==0:
            res = n.val
            if n.right:
                self.stack.append((n.right, -1))
                while True:
                    n, act = self.stack.pop()
                    self.stack.append((n, 0))
                    if not n.left:
                        break
                    self.stack.append((n.left, -1))
            return res
            
if __name__ == "__main__":
    root = BSTIterator(
        TreeNode(6, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(5, TreeNode(4))))
    )
    while root.hasNext(): 
        print(root.next())
