# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        nNode = head.next #next node
        head.next = None
        pNode = head #previous node
        cNode = nNode #current node
        while nNode is not None:
            nNode = cNode.next
            cNode.next = pNode
            pNode = cNode
            cNode = nNode
        head = pNode
        return head