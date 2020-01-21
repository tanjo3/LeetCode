# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        curr_level = [root]
        btlo = []

        while len(curr_level) > 0:
            next_level = []
            level = []
            while len(curr_level) > 0:
                node = curr_level.pop()
                level.append(node.val)

                if node.left is not None:
                    next_level.append(node.left)

                if node.right is not None:
                    next_level.append(node.right)

            btlo.insert(0, level)

            curr_level = next_level
            curr_level.reverse()

        return btlo
