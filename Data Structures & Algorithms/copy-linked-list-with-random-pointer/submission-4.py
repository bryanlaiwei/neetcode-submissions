"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        headCp, headCp2, newHead = head, head, Node(0)

        while head:
            nodeCp = Node(head.val, head.next, None)
            head.next = nodeCp
            head = head.next.next
        
        while headCp:
            if headCp.random: headCp.next.random = headCp.random.next
            headCp = headCp.next.next
        
        if headCp2: 
            newHead = headCp2.next

            while headCp2:
                temp = headCp2.next.next
                if temp: headCp2.next.next = headCp2.next.next.next
                headCp2.next = temp
                headCp2 = headCp2.next
        
            return newHead
        
        return head
            
            