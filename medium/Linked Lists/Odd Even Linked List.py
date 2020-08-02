# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        p1 = head
        if not p1.next:
            return head
        p2 = p1.next
        head2 = p2
        if not p2.next:
            return head
        while p2 and p2.next:
            p3 = p2.next
            p1.next = p3
            p2.next = p3.next
            p1 = p1.next
            p2 = p2.next
        p1.next = head2
        return head