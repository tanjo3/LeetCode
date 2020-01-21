# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def rec_check(t1, t2) -> bool:
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            else:
                return t1.val == t2.val and \
                    rec_check(t1.left, t2.left) and \
                    rec_check(t1.right, t2.right)

        return rec_check(p, q)
