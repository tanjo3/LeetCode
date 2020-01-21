# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        carry = 0

        while not (l1 is None and l2 is None):
            if l2 is None:
                sum = l1.val + carry
                l1 = l1.next
            elif l1 is None:
                sum = l2.val + carry
                l2 = l2.next
            else:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            carry = sum // 10

            if head is None:
                head = ListNode(sum % 10)
                curr = head
            else:
                curr.next = ListNode(sum % 10)
                curr = curr.next

        if carry != 0:
            curr.next = ListNode(carry)

        return head
