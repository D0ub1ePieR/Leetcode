# 21、合并两个有序链表
> tag: python 、 链表

***
### 题目描述

&emsp;&emsp;将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

### 示例

```
  输入：1->2->4, 1->3->4
  输出：1->1->2->3->4->4
```

***
### 题目链接
[21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

***
### 题解

&emsp;&emsp;很简单的一道题，只需要每次取 `l1, l2` 当前指向的值最小的一个加入到结果链表中，当 `l1, l2`中有一个到链表尾部时，将另一个没到链表尾部的剩余部分加入到结果中并返回。

```python
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
```

&emsp;&emsp;最终结果，*运行时间44ms*，超过51.81%；*占用内存13.7MB*，超过5.05%。
