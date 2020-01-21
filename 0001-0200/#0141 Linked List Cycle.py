# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        seen = []
        curr = head
        while curr is not None:
            if curr in seen:
                return True
            else:
                seen.append(curr)
            curr = curr.next

        return False
