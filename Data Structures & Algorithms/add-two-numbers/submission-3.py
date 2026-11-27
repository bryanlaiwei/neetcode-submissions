# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = last = ListNode()
        carry = 0

        while l1 or l2 or carry:
            if l1: l1Val = l1.val
            else: l1Val = 0
            if l2: l2Val = l2.val
            else: l2Val = 0

            if carry:
                last.next = ListNode(val = 1, next = None)
                carry = 0
            else: last.next = ListNode(val = 0, next = None)

            last = last.next
            last.val += (l1Val + l2Val) % 10

            if last.val >= 10: 
                last.val = 0
                carry = 1
            if l1Val + l2Val >= 10: carry = 1
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return start.next
