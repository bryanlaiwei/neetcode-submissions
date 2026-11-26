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
        nodeDict = {None: None}
        dummy = newHead = Node(0)
        headcpy = head

        while headcpy:
            if headcpy.random and headcpy.random not in nodeDict:
                nodeDict[headcpy.random] = Node(headcpy.random.val, None, None)
            if headcpy.next and (headcpy.next) not in nodeDict:
                nodeDict[headcpy.next] = Node(headcpy.next.val, None, None)
            if headcpy not in nodeDict: 
                nodeDict[headcpy] = Node(headcpy.val, None, None)
            
            headcpy = headcpy.next
        
        while head:
            newNext, newRandom = None, None
            newNext = nodeDict[head.next]
            newRandom = nodeDict[head.random]
            nodeDict[head].next = newNext
            nodeDict[head].random = newRandom
            newHead.next = nodeDict[head]
            newHead = newHead.next
            head = head.next
        
        return dummy.next
            