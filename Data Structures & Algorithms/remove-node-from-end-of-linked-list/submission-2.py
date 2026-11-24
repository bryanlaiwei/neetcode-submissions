# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, fast, iterator, count = ListNode(), head, head, 0
        dummy.next = head
        slow = dummy

        while iterator:
            count += 1
            if count == n: 
                fast = iterator
                break
            iterator = iterator.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next