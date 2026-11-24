# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast, iterator, dummy, slowPrev = head, head, head, ListNode(), None
        dummy.next = slow
        count = 0

        while iterator:
            count += 1
            if count == n: 
                fast = iterator
                break
            iterator = iterator.next

        while fast.next:
            fast = fast.next
            slowPrev = slow
            slow = slow.next
            slowPrev.next = slow
            # print(slow.val, fast)
        
        if not slowPrev: return slow.next
        slowPrev.next = slow.next
        return dummy.next