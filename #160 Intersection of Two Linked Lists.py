# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode
                            ) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            curr = head

            while curr is not None:
                curr = curr.next
                length += 1

            return length

        lenA = getLength(headA)
        lenB = getLength(headB)

        currA = headA
        currB = headB

        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA is not currB:
            currA = currA.next
            currB = currB.next

        return currA
