# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalfStart = slow.next
        slow.next = None

        prev, curr = None, secondHalfStart
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        secondHalfStart = prev

        while secondHalfStart:
            temp = head.next
            head.next = secondHalfStart
            secondHalfStart = secondHalfStart.next
            head = head.next
            head.next = temp
            head = head.next
        
        
