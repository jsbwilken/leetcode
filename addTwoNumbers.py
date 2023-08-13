#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            if carry != 0:
                return ListNode(carry, None)
            else:
                return None

        if l1 is None:
            val1 = 0
            next1 = None
        else:
            val1 = l1.val
            next1 = l1.next

        if l2 is None:
            val2 = 0
            next2 = None
        else:
            val2 = l2.val
            next2 = l2.next

        carry_next = (val1 + val2 + carry) // 10

        return ListNode((val1 + val2 + carry) % 10, self.addTwoNumbers(next1, next2, carry_next))

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

l3 = Solution().addTwoNumbers(l1, l2)
pass