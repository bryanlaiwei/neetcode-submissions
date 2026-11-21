# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowNode, fastNode = head, head

        while fastNode and fastNode.next and fastNode.next.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next

            if slowNode == fastNode: return True
        
        return False