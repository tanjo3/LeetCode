# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def sym_check(t1, t2) -> bool:
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            else:
                return t1.val == t2.val and \
                    sym_check(t1.left, t2.right) and \
                    sym_check(t1.right, t2.left)

        return sym_check(root.left, root.right)
