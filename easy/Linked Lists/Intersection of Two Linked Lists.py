# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        nodeA = headA
        nodeB = headB
        
        while nodeA is not None or nodeB is not None:
            if nodeA is None:
                nodeA = headB
            if nodeB is None:
                nodeB = headA
            
            if nodeA == nodeB:
                return nodeA
            
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        return None