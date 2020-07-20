# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        head = None
        current_node = None
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                #put l1 and move the l1 pointer
                next_node = l1
                l1 = l1.next
            else:
                #put l2 and move the l2 pointer
                next_node = l2
                l2 = l2.next
            if current_node is None:
                head = current_node = next_node
            else:
                current_node.next = next_node
                current_node = current_node.next
        
        if l1 is None:
            current_node.next = l2
        if l2 is None:
            current_node.next = l1
        
        return head