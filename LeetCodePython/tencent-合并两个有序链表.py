# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        while l2!=None:
            p=l1
            if p.val>=l2.val:
                t=l2
                l2=l2.next
                t.next=p
                l1=t
                continue
            while p.next!=None:
                if p.next.val>l2.val:
                    t=l2
                    l2=l2.next
                    t.next=p.next
                    p.next=t
                    break
                p=p.next
            if p.next==None:
                p.next=l2
                l2=l2.next
                p.next.next=None
        return l1
# 12.42
