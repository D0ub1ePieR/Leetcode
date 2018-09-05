# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        p=head.next
        phead=head
        while p!=None:
            head.next=p.next
            p.next=phead
            phead=p
            p=head.next
        return phead
# 96.86
