#
#  Create by Hua on 8/31/2016
#


"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

"""


# 64 ms, linked list remove node
from N0_DataStructures import ListNode
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        tail = head
        while n>0:
            tail = tail.next
            n -= 1

        if tail is None:
            return head.next
        else:
            t = head
            while tail.next is not None:
                t = t.next
                tail = tail.next

            t.next = t.next.next
            return head
