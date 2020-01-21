# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        next_val = 0

        while not (l1 is None and l2 is None):
            if l2 is None:
                next_val = l1.val
                l1 = l1.next
            elif l1 is None:
                next_val = l2.val
                l2 = l2.next
            else:
                if l1.val < l2.val:
                    next_val = l1.val
                    l1 = l1.next
                else:
                    next_val = l2.val
                    l2 = l2.next

            if head is None:
                head = ListNode(next_val)
                curr = head
            else:
                curr.next = ListNode(next_val)
                curr = curr.next

        return head
