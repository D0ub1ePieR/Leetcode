class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class solution:
    def removeNthFromEnd(self,head,n):
        if head.next==None:
            return None
        fst=head
        scd=head
        for i in range(n):
            fst=fst.next
        if fst==None:
            return head.next
        while fst.next!=None:
            fst=fst.next
            scd=scd.next
        scd.next=scd.next.next
        return head
    
t=solution()
l=ListNode(1)
l2=ListNode(2)
l.next=l2
print(t.removeNthFromEnd(l,2).val)
