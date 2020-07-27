# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        mid = head
        cnode1 = head
        while cnode1 and cnode1.next:
            cnode1 = cnode1.next.next
            mid = mid.next
        
        cnode1 = head
        cnode2 = self.reverse(mid)
        
        while cnode1 and cnode2:
            if cnode1.val != cnode2.val:
                return False
            cnode1 = cnode1.next
            cnode2 = cnode2.next
        
        return True
    
    def reverse(self, head):
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