# python3
# simple
# 链表
# 44ms 51.81%
# 13.7MB 5.05%

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        home = l
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                l.next = ListNode(l1.val)
                l = l.next
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l = l.next
                l2 = l2.next
        if l1 != None:
            l.next = l1
        if l2 != None:
            l.next = l2
        return home.next
