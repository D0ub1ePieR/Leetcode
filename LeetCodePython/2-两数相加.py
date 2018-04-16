# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag=0
        sol=l1
        while True:
            t=l1.val+l2.val+flag
            flag=t//10
            l1.val=t%10
            if l1.next==None and l2.next==None:
                if flag==1:
                    l1.next=ListNode(1)
                return sol
            if l1.next==None:
                if flag==1:
                    t=l2.next
                    while t.val==9:
                        t.val=0
                        if t.next==None:
                            t.next=ListNode(1)
                            l1.next=l2.next
                            return sol
                        else:
                            t=t.next
                    t.val=t.val+1
                l1.next=l2.next
                return sol
            if l2.next==None:
                if flag==1:
                    t=l1.next
                    while t.val==9:
                        t.val=0
                        if t.next==None:
                            t.next=ListNode(1)
                            return sol
                        else:
                            t=t.next
                    t.val=t.val+1
                return sol
            l1=l1.next
            l2=l2.next
