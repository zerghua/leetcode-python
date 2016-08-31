#
#  Create by Hua on 8/31/2016
#


"""

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""

from N0_DataStructures import ListNode

# 64
# merge two linked lists, use dummy node.
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        cur = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1 is not None: cur.next = l1
        if l2 is not None: cur.next = l2
        return dummy.next