# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        prev_val = head.val

        tail = head
        curr = head.next

        while curr is not None:
            if curr.val != prev_val:
                tail.next = curr
                prev_val = curr.val
                tail = curr
            curr = curr.next
        tail.next = None

        return head
