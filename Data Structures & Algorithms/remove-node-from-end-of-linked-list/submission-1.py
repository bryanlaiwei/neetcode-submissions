# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast, iterator, count = ListNode, head, head, 0
        slow.next = head

        while iterator:
            count += 1
            if count == n: 
                fast = iterator
                break
            iterator = iterator.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        if slow.next == head: return head.next
        slow.next = slow.next.next
        return head