# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(x) -> int:
            if x is None:
                return 0
            else:
                return 1 + max(height(x.left), height(x.right))

        if root is None:
            return True
        else:
            return self.isBalanced(root.left) and \
                self.isBalanced(root.right) and \
                abs(height(root.left) - height(root.right)) < 2
